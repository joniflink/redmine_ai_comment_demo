Rails.application.routes.draw do
  post 'ai_comment/issues/:id/apply_priority',
    to: 'ai_comment#apply_priority'
end
