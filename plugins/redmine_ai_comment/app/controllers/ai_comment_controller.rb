class AiCommentController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :find_issue
  before_action :authorize_global

  def apply_priority
    Rails.logger.info("[AI_COMMENT] apply_priority called")
    Rails.logger.info("[AI_COMMENT] issue_id: #{@issue.id}")
    Rails.logger.info("[AI_COMMENT] apply_action: #{params[:apply_action]}")

    case params[:apply_action]
    when "apply"
      priority = IssuePriority.find_by(id: params[:priority_id].to_i)
      
      unless priority
        Rails.logger.error("[AI_COMMENT] Invalid priority_id: #{params[:priority_id]}")
        flash[:error] = "Invalid AI priority suggestion."
        redirect_to issue_path(@issue)
        return
      end

      Rails.logger.info("[AI_COMMENT] Applying priority #{priority.id} #{priority.name}")

      old_priority_name = @issue.priority&.name
      @issue.priority = priority
      clear_ai_priority_suggestion

      if @issue.save
        Rails.logger.info("[AI_COMMENT] Priority change successful.")
        @issue.init_journal(User.current, "AI suggestion applied: priority changed from #{old_priority_name} to #{priority.name}")
        flash[:notice] = "AI suggestion applied."
      else
        Rails.logger.error("[AI_COMMENT] Save failed: #{@issue.errors.full_messages.join(', ')}")
        flash[:error] = "Could not apply AI suggestion."
      end

      redirect_to issue_path(@issue)

    when "cancel"
      clear_ai_priority_suggestion
      
      if @issue.save
        Rails.logger.info("[AI_COMMENT] AI suggestion dismissed.")
        flash[:notice] = "AI suggestion dismissed."
      else
        Rails.logger.error("[AI_COMMENT] Save failed: #{@issue.errors.full_messages.join(', ')}")
        flash[:error] = "Could not dismiss AI suggestion"
      end

      redirect_to issue_path(@issue)

    else
      Rails.logger.error("[AI_COMMENT] apply_action not implemented: #{params[:apply_action]}")
      flash[:error] = "Invalid action"
      redirect_to issue_path(@issue)
    end
  end

  private

  def clear_ai_priority_suggestion
    @issue.custom_field_values.each do |value|
      if value.custom_field.name == ai_priority_custom_field_name
        value.value = nil
        Rails.logger.info("[AI_COMMENT] Custom field value cleared.")
      end
    end
  end

  def find_issue
    @issue = Issue.find(params[:id])
  end

  def ai_priority_custom_field_name
    ENV.fetch("AI_PRIORITY_CUSTOM_FIELD_NAME")
  end
end
