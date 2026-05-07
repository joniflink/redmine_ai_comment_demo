class AiHookListener < Redmine::Hook::Listener
  def controller_issues_new_after_save(context = {})
    issue = context[:issue]
    Rails.logger.info("[AI PLUGIN] Hook triggered for issue #{issue.id}")
    
    script = "/usr/src/redmine/plugins/redmine_ai_comment/lib/ai_comment.py"
    cmd = "python3 #{script} #{issue.id} 2>&1"

    output = `#{cmd}`
    status = $?.exitstatus

    Rails.logger.info("[AI PLUGIN] Command: #{cmd}")
    Rails.logger.info("[AI PLUGIN] Exit status: #{status}")
    Rails.logger.info("[AI PLUGIN] Output: #{output}")
  rescue => e
    Rails.logger.error("[AI PLUGIN] Exception: #{e.class}: #{e.message}")
    Rails.logger.error(e.backtrace.join("\n"))
  end

  def view_issues_show_details_bottom(context = {})
    issue = context[:issue]

    field = issue.custom_field_values.find do |value|
      value.custom_field.name == "AI suggested priority id"
    end

    return "" if field.nil?
    return "" if field.value.blank?

    priority_id = field.value

    context[:controller].send(
      :render_to_string,
      inline: <<~ERB,
        <div class="box">
          <strong>AI Comment</strong>
          <p>AI has suggested priority change for this issue.</p>
          <%= button_to "Apply AI suggestion",
            "/ai_comment/issues/#{issue.id}/apply_priority",
            method: :post,
            params: {priority_id: #{priority_id}},
            class: "button" %>
        </div>
      ERB
    )
  end

  def view_layouts_base_html_head(context = {})
    <<~HTML
      <style>
        .cf_1,
        #issue_custom_field_values_1,
        label[for="issue_custom_field_values_1"] {
          display: none !important;
        }
      </style>
    HTML
  end
end
