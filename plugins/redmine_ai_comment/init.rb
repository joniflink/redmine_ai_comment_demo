require 'redmine'
require_dependency File.expand_path('lib/ai_hook_listener', __dir__)

Redmine::Plugin.register :redmine_ai_comment do
  name 'Redmine AI Comment'
  author 'Joni Flink'
  description 'AI integration for issue analysis'
  version '0.0.1'
end
