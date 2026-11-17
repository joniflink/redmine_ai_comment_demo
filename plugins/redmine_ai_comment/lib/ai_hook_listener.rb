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
      value.custom_field.name == ai_priority_custom_field_name
    end

    return "" if field.nil?
    return "" if field.value.blank?

    priority_id = field.value

    return "" if issue.priority_id.to_s == priority_id.to_s

    priority_name = IssuePriority.find_by(id: priority_id)

    context[:controller].send(
      :render_to_string,
      inline: <<~ERB,
        <div class="box">
          <strong>AI Comment</strong>
          <p>AI suggests priority change to #{priority_name}.</p>

          <%= button_to "Apply AI suggestion",
            "/ai_comment/issues/#{issue.id}/apply_priority",
            method: :post,
            params: {
              apply_action: "apply",
              priority_id: #{priority_id}
            },
            class: "button" %>

          <%= button_to "Cancel",
            "/ai_comment/issues/#{issue.id}/apply_priority",
            method: :post,
            params: {
              apply_action: "cancel"
            },
            class: "button" %>
        </div>
      ERB
    )
  end

  def view_layouts_base_html_head(context = {})
    field = ai_priority_custom_field
    return "" unless field

    <<~HTML
      <style>
        .cf_#{field.id},
        #issue_custom_field_values_#{field.id},
        label[for="issue_custom_field_values_#{field.id}"] {
          display: none !important;
        }
      </style>
    HTML
  end

  def ai_priority_custom_field_name
    ENV.fetch("AI_PRIORITY_CUSTOM_FIELD_NAME")
  end

  def ai_priority_custom_field
    IssueCustomField.find_by(name: ai_priority_custom_field_name)
  end
end
