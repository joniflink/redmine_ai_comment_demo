class AiCommentController < ApplicationController
  skip_before_action :verify_authenticity_token
  before_action :find_issue
  before_action :authorize_global

  protect_from_forgery with: :exception

  def apply_priority
    Rails.logger.info("[AI_COMMENT] apply_priority called")
    Rails.logger.info("[AI_COMMENT] issue id: #{@issue.id}")
    Rails.logger.info("[AI_COMMENT] params: #{params.inspect}")

    priority_id = params[:priority_id].to_i
    priority = IssuePriority.find_by(id: priority_id)

    unless priority
      Rails.logger.error("[AI_COMMENT] Invalid priority_id: #{params[:priority_id]}")
      flash[:error] = "Invalid AI priority suggestion."
      redirect_to issue_path(@issue)
      return
    end

    old_priority = @issue.priority&.name
    @issue.priority = priority
    clear_ai_priority_suggestion

    if @issue.save
      Rails.logger.info("[AI_COMMENT] Priority changed to #{priority.name}")
      @issue.init_journal(User.current, "AI suggestion applied: priority changed from #{old_priority} to #{priority.name}.")
      flash[:notice] = "AI suggestion applied."
    else
      Rauks.logger.error("[AI_COMMENT] Save failed: #{@issue.errors.full_messages.join(', ')}")
      flash[:error] = "Could not apply AI suggestion."
    end

    redirect_to issue_path(@issue)
  end

  private

  def find_issue
    @issue = Issue.find(params[:id])
  end

  def clear_ai_priority_suggestion
    custom_field = IssueCustomField.find_by(name: "AI suggested priority id")
    return unless custom_field

    @issue.custom_field_values = {
      custom_field.id.to_s => ""
    }
  end
end
