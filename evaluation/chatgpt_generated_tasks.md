# Customer Portal Revamp --- Redmine Example Issues

A fictional software project backlog containing 64 example issues for
use in Redmine.

## Project overview

-   **Project:** Customer Portal Revamp
-   **Description:** Upgrade the existing customer portal with improved
    UX, performance optimizations, and new account management features.
-   **Start date:** 2026-03-01
-   **End date:** 2026-06-30
-   **Modules:** Authentication, Dashboard, Billing, Notifications, API
-   **Trackers used:** Bug, Feature, Task, Support

------------------------------------------------------------------------

## Issue 1 --- Login fails with valid credentials

-   **Tracker:** Bug
-   **Status:** In Progress
-   **Priority:** High
-   **Assignee:** Alice Mäkinen
-   **Start date:** 2026-03-05
-   **Due date:** 2026-03-10

**Description:**\
Users report intermittent login failures despite correct credentials.
Likely related to session handling.

## Issue 2 --- Implement user profile page

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-03-08
-   **Due date:** 2026-03-25

**Description:**\
Create a profile page where users can update personal details, password,
and notification preferences.

## Issue 3 --- Dashboard loads slowly

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-03-07
-   **Due date:** 2026-03-15

**Description:**\
Initial dashboard load takes over 5 seconds. Needs performance
optimization.

## Issue 4 --- Set up CI/CD pipeline

-   **Tracker:** Task
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-03-01
-   **Due date:** 2026-03-20

**Description:**\
Configure automated build, test, and deployment pipeline using GitHub
Actions.

## Issue 5 --- Add billing history view

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-03-12
-   **Due date:** 2026-04-05

**Description:**\
Allow users to view past invoices and download PDF receipts.

## Issue 6 --- Email notifications not sent

-   **Tracker:** Bug
-   **Status:** Resolved
-   **Priority:** Urgent
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-03-03
-   **Due date:** 2026-03-06

**Description:**\
System fails to send email notifications due to SMTP misconfiguration.

## Issue 7 --- API returns 500 on invalid input

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** High
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-03-09
-   **Due date:** 2026-03-14

**Description:**\
API should return proper validation errors instead of generic server
error.

## Issue 8 --- Write user documentation

-   **Tracker:** Task
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-03-15
-   **Due date:** 2026-04-10

**Description:**\
Prepare end-user documentation for new portal features.

## Issue 9 --- Password reset link expires too quickly

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Alice Mäkinen
-   **Start date:** 2026-03-16
-   **Due date:** 2026-03-18

**Description:**\
Users report that password reset links expire within a few minutes
instead of the intended 24-hour validity period.

## Issue 10 --- Add two-factor authentication (2FA)

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-03-20
-   **Due date:** 2026-04-15

**Description:**\
Implement optional two-factor authentication using email codes and
authenticator apps to improve account security.

## Issue 11 --- Refactor authentication module

-   **Tracker:** Task
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-03-18
-   **Due date:** 2026-04-01

**Description:**\
Clean up legacy authentication code, remove duplication, and improve
maintainability and test coverage.

## Issue 12 --- Session timeout not enforced

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-03-17
-   **Due date:** 2026-03-22

**Description:**\
Users remain logged in longer than the configured session timeout,
posing a potential security risk.

## Issue 13 --- Dark mode support

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-03-25
-   **Due date:** 2026-04-20

**Description:**\
Provide an optional dark theme for the portal to improve usability in
low-light environments.

## Issue 14 --- Customer unable to update billing information

-   **Tracker:** Support
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-03-19
-   **Due date:** 2026-03-21

**Description:**\
A customer reports receiving an error when attempting to update credit
card details. Needs investigation and resolution.

## Issue 15 --- Incorrect currency displayed in invoices

-   **Tracker:** Bug
-   **Status:** Resolved
-   **Priority:** Normal
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-03-10
-   **Due date:** 2026-03-13

**Description:**\
Some invoices incorrectly display USD instead of EUR for European
customers. Issue has been fixed but should be verified.

## Issue 16 --- Clean up unused API endpoints

-   **Tracker:** Task
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-03-22
-   **Due date:** 2026-04-05

**Description:**\
Identify and remove deprecated API endpoints that are no longer used by
the frontend or external integrations.

## Issue 17 --- Export dashboard data to CSV

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-03-28
-   **Due date:** 2026-04-18

**Description:**\
Allow users to export dashboard metrics and reports into CSV format for
external analysis.

## Issue 18 --- Duplicate email notifications sent

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-03-21
-   **Due date:** 2026-03-26

**Description:**\
Users sometimes receive duplicate email notifications for the same
event. Likely related to event handling or retry logic.

## Issue 19 --- Audit logging missing for critical user actions

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-02
-   **Due date:** 2026-04-20

**Description:**\
Currently, the system does not consistently log critical user actions
such as password changes, email updates, or billing modifications. This
creates gaps in traceability and makes it difficult to investigate
security incidents or user-reported issues.

Implement a centralized audit logging mechanism that records key events
with timestamps, user IDs, IP addresses, and relevant metadata. Logs
should be queryable via an admin interface and optionally exportable for
compliance purposes. Consider performance impact and storage retention
policies.

## Issue 20 --- Intermittent failure when saving notification preferences

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Normal
-   **Assignee:** Maria Laine
-   **Start date:** 2026-04-01
-   **Due date:** 2026-04-07

**Description:**\
Some users report that changes to notification preferences (email
vs. in-app notifications) are not always persisted. The issue appears
intermittently and may be related to race conditions or failed API calls
that are not properly surfaced to the UI.

Investigate backend logs and frontend request handling. Ensure proper
error handling and user feedback if saving fails. Add automated tests to
cover this scenario.

## Issue 21 --- Improve accessibility (WCAG compliance)

-   **Tracker:** Task
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-04-03
-   **Due date:** 2026-04-30

**Description:**\
The current UI does not fully meet accessibility standards (WCAG 2.1).
Issues include insufficient color contrast, missing ARIA labels, poor
keyboard navigation, and inconsistent focus states.

Perform a full accessibility audit and implement improvements across the
portal. Focus especially on login, dashboard, and billing sections.
Document changes and provide guidelines for future development to
maintain compliance.

## Issue 22 --- Data inconsistency between dashboard and billing module

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-05
-   **Due date:** 2026-04-12

**Description:**\
Users have reported discrepancies between account balances shown on the
dashboard and those displayed in the billing section. This may be caused
by caching issues, delayed synchronization, or differences in
calculation logic between services.

Investigate data flow between services and ensure consistency. Align
calculation methods and consider introducing a single source of truth
for financial data.

## Issue 23 --- Add rate limiting to public API endpoints

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-06
-   **Due date:** 2026-04-18

**Description:**\
Public API endpoints currently do not enforce rate limits, making them
vulnerable to abuse or accidental overuse. This could lead to degraded
performance or denial-of-service scenarios.

Implement configurable rate limiting per API key or IP address. Provide
meaningful error responses when limits are exceeded. Ensure that limits
are documented and adjustable without redeploying the application.

## Issue 24 --- Mobile layout breaks on small screens

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Normal
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-04-04
-   **Due date:** 2026-04-09

**Description:**\
On devices with small screen sizes (e.g., older smartphones), parts of
the UI overflow or become unusable. Issues include clipped buttons,
overlapping text, and horizontal scrolling.

Review responsive design implementation and fix layout issues across key
pages. Test on a range of screen sizes and browsers to ensure consistent
behavior.

## Issue 25 --- Introduce feature flags for gradual rollouts

-   **Tracker:** Task
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-07
-   **Due date:** 2026-04-25

**Description:**\
Deployments currently release features to all users at once, increasing
risk when introducing new functionality.

Implement a feature flag system that allows selective enabling/disabling
of features for specific user groups or environments. This will support
safer rollouts, A/B testing, and quicker rollback in case of issues.

## Issue 26 --- Search functionality returns incomplete results

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-04-03
-   **Due date:** 2026-04-10

**Description:**\
Users report that search results do not include all expected items,
particularly when using partial keywords or filters. This may be due to
indexing delays or limitations in the search implementation.

Review search indexing logic and improve matching algorithms. Consider
adding fuzzy search or better filtering options. Validate results
against database queries.

## Issue 27 --- Add onboarding tutorial for new users

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-04-10
-   **Due date:** 2026-05-05

**Description:**\
New users often struggle to understand key features of the portal,
leading to increased support requests.

Design and implement a lightweight onboarding experience, such as guided
tooltips or a walkthrough, to highlight important functionality. Ensure
it can be skipped or revisited later.

## Issue 28 --- Background jobs occasionally fail without retry

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-02
-   **Due date:** 2026-04-11

**Description:**\
Some background jobs (e.g., email sending, report generation) fail
silently without retrying. This leads to missing notifications and
incomplete data processing.

Investigate job queue configuration and implement retry logic with
exponential backoff. Add monitoring and alerting for repeated failures.

## Issue 29 --- Timezone inconsistencies in scheduled notifications

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-04-08
-   **Due date:** 2026-04-14

**Description:**\
Scheduled notifications (e.g., billing reminders, account alerts) are
being sent at incorrect times for users in different timezones. Initial
investigation suggests that the backend stores timestamps in UTC, but
frontend scheduling logic and some cron jobs may be using local server
time.

This results in users receiving notifications several hours early or
late, which has already caused confusion around billing deadlines.

Standardize timezone handling across the system (preferably UTC
internally with proper conversion at display time). Audit all scheduled
jobs and add automated tests to ensure consistent behavior across
timezones.

## Issue 30 --- File upload fails silently for large attachments

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-09
-   **Due date:** 2026-04-13

**Description:**\
Users attempting to upload large files (e.g., \>10MB) sometimes
experience silent failures where the upload appears to complete but the
file is not stored or linked correctly. No error message is shown in the
UI.

Possible causes include server-side size limits, reverse proxy
configuration, or timeout issues.

Add proper validation and user feedback for file size limits, ensure
backend returns clear error responses, and verify infrastructure
configuration supports intended limits.

## Issue 31 --- Improve error handling consistency across API

-   **Tracker:** Task
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-10
-   **Due date:** 2026-04-28

**Description:**\
API error responses are currently inconsistent in structure and
messaging. Some endpoints return structured JSON errors, while others
return plain text or generic HTTP 500 responses.

This inconsistency complicates frontend error handling and makes
debugging harder for integrators.

Define and enforce a unified error response format (including error
codes, messages, and optional metadata). Refactor existing endpoints and
update documentation accordingly.

## Issue 32 --- Duplicate user accounts created via race condition

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Urgent
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-07
-   **Due date:** 2026-04-10

**Description:**\
Under certain conditions (e.g., slow network or repeated form
submissions), duplicate user accounts can be created with the same email
address. This indicates a race condition where uniqueness constraints
are not properly enforced at the database or application level.

This is a critical issue affecting data integrity and user experience.

Add proper database constraints, implement idempotent request handling,
and ensure frontend prevents duplicate submissions.

## Issue 33 --- Admin dashboard lacks filtering options

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-04-12
-   **Due date:** 2026-05-02

**Description:**\
The admin dashboard currently displays large amounts of data (users,
transactions, logs) without sufficient filtering or search capabilities.
This makes it difficult for administrators to locate specific records or
analyze trends.

Introduce filtering by date range, status, user role, and other relevant
attributes. Consider adding saved filters and export functionality for
reporting purposes.

## Issue 34 --- Memory usage spikes under heavy load

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-11
-   **Due date:** 2026-04-18

**Description:**\
During load testing, application memory usage increases steadily and
does not return to baseline after traffic subsides. This suggests a
potential memory leak or inefficient caching strategy.

If left unresolved, this could lead to degraded performance or crashes
in production.

Profile the application under load, identify problematic components, and
optimize memory management. Add monitoring to detect similar issues in
the future.

## Issue 35 --- Email templates not localized

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-04-15
-   **Due date:** 2026-05-10

**Description:**\
System-generated emails (e.g., welcome messages, password resets,
invoices) are currently only available in English, even for users with
different locale settings.

Implement localization support for email templates, including
translation management and fallback behavior. Ensure that language
selection aligns with user preferences stored in the system.

## Issue 36 --- Broken links in user documentation

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** Low
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-04-10
-   **Due date:** 2026-04-16

**Description:**\
Several links in the user documentation lead to outdated or non-existent
pages, particularly after recent restructuring of the help section.

This negatively impacts user experience and increases support requests.

Perform a full audit of documentation links and implement automated link
checking as part of the documentation workflow.

## Issue 37 --- Add pagination to transaction history

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-04-13
-   **Due date:** 2026-04-27

**Description:**\
Transaction history currently loads all records at once, which leads to
slow performance and poor usability for users with large datasets.

Implement pagination or infinite scrolling, along with sorting and
filtering options. Ensure backend supports efficient querying with
limits and offsets.

## Issue 38 --- Logging system generates excessive noise

-   **Tracker:** Task
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-14
-   **Due date:** 2026-04-30

**Description:**\
Current logging includes a large volume of low-value debug messages in
production, making it difficult to identify important events or errors.

Review logging levels and reduce noise by adjusting verbosity. Introduce
structured logging and consider log aggregation tools for better
analysis.

## Issue 39 --- Third-party payment gateway timeout handling

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-12
-   **Due date:** 2026-04-17

**Description:**\
When the third-party payment gateway times out, the system does not
handle the failure gracefully. Users may see unclear error messages or
be left uncertain whether their payment was processed.

Implement proper timeout handling, retries where appropriate, and clear
user feedback. Ensure idempotency to avoid duplicate charges.

## Issue 40 --- Add system health monitoring dashboard

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-16
-   **Due date:** 2026-05-08

**Description:**\
There is currently no centralized view of system health (e.g., uptime,
error rates, queue lengths). This makes it difficult for the team to
proactively detect and respond to issues.

Build an internal dashboard that aggregates key metrics from various
services. Include alerting thresholds and visualizations to support
operational monitoring.

## Issue 41 --- User sessions invalidated unexpectedly after deployment

-   **Tracker:** Bug
-   **Status:** In Progress
-   **Priority:** High
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-18
-   **Due date:** 2026-04-22

**Description:**\
Following recent deployments, active user sessions are sometimes
invalidated unexpectedly, forcing users to log in again. The issue
appears inconsistent and may depend on which application node handles
the request after deployment.

Preliminary investigation suggests that session serialization or signing
keys may differ between instances during rolling deployments. This
causes session validation failures when traffic shifts between nodes.

Investigate deployment configuration, session storage strategy, and
cache invalidation behavior. The goal is to ensure seamless deployments
without interrupting active user sessions.

## Issue 42 --- Legacy browser support issues in billing module

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** Low
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-04-19
-   **Due date:** 2026-04-26

**Description:**\
Some customers using older browsers report broken layouts and
non-functional buttons within the billing module. The issue seems
particularly common in older Safari and Internet Explorer compatibility
modes still used in corporate environments.

While official support for outdated browsers is limited, the current
behavior is significantly degraded and may affect paying enterprise
customers.

Review frontend compatibility, identify unsupported JavaScript or CSS
features, and determine whether graceful degradation or polyfills should
be implemented.

## Issue 43 --- Scheduled reports generated with stale cached data

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Normal
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-20
-   **Due date:** 2026-04-24

**Description:**\
Automatically generated reports occasionally include outdated
information even though the underlying records have been updated. This
issue appears related to application-level caching that is not properly
invalidated before report generation.

Customers have noticed discrepancies between dashboard metrics and
exported reports, reducing trust in reporting accuracy.

Review cache invalidation logic and ensure report jobs always use fresh
data sources where accuracy is critical.

## Issue 44 --- Add support for account activity history

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-04-21
-   **Due date:** 2026-05-12

**Description:**\
Customers have requested visibility into recent account activity,
including login attempts, password changes, profile updates, and billing
actions.

Implement an "Account Activity" page that displays a chronological
history of important user actions. Include timestamps, device/browser
information where available, and indicators for suspicious activity.

Consider privacy implications and define a retention policy for
historical records.

## Issue 45 --- Search indexing job causes database spikes

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-22
-   **Due date:** 2026-04-29

**Description:**\
The nightly search indexing job places significant load on the primary
database, resulting in increased response times and temporary API
slowdowns during peak indexing periods.

Monitoring data shows large sequential reads and long-running queries
associated with index refresh operations.

Investigate opportunities to optimize indexing queries, reduce locking,
or move indexing to a replica database. The indexing process should
minimize impact on production traffic.

## Issue 46 --- Users not redirected correctly after SSO login

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-04-23
-   **Due date:** 2026-04-28

**Description:**\
Users authenticating through Single Sign-On (SSO) are occasionally
redirected to the default dashboard instead of the originally requested
page. This disrupts workflows and causes confusion, especially for
bookmarked deep links.

The issue may be related to lost redirect parameters during
authentication handoff or session initialization timing.

Ensure redirect targets are preserved securely throughout the
authentication process and validate against potential open redirect
vulnerabilities.

## Issue 47 --- Improve onboarding flow for invited team members

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Low
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-04-24
-   **Due date:** 2026-05-14

**Description:**\
New team members invited into shared accounts often struggle to
understand their permissions and initial setup steps. This results in
avoidable support tickets and delayed adoption.

Improve the onboarding flow by adding contextual guidance, clearer role
descriptions, and a checklist for first-time setup actions.

Consider collecting feedback from newly invited users to identify the
most confusing parts of the current experience.

## Issue 48 --- Excessive retries during webhook delivery failures

-   **Tracker:** Bug
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-21
-   **Due date:** 2026-04-27

**Description:**\
Failed webhook deliveries are currently retried too aggressively,
occasionally overwhelming customer endpoints and generating unnecessary
traffic.

Some integrations temporarily block requests due to the high retry
frequency, which further amplifies delivery failures.

Implement exponential backoff and configurable retry policies. Add
better observability around webhook delivery status and failure causes.

## Issue 49 --- Dashboard widgets do not persist custom order

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** Low
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-04-22
-   **Due date:** 2026-04-25

**Description:**\
Users can rearrange dashboard widgets via drag-and-drop, but the custom
order is not reliably preserved after page refresh or logout.

In some cases the layout resets completely, while in others only partial
changes are saved.

Investigate frontend state persistence and backend preference storage.
Add automated tests for widget configuration persistence.

## Issue 50 --- Introduce soft-delete support for customer records

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-25
-   **Due date:** 2026-05-16

**Description:**\
Customer records are currently permanently deleted, making accidental
removals difficult to recover from and complicating compliance
workflows.

Introduce soft-delete functionality so records can be marked as deleted
while remaining recoverable for a configurable retention period.

Ensure deleted records are excluded from normal application views while
remaining accessible to administrators for recovery or auditing
purposes.

## Issue 51 --- API documentation out of sync with implementation

-   **Tracker:** Task
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-04-24
-   **Due date:** 2026-05-03

**Description:**\
Several API endpoints behave differently from what is described in the
public documentation. Missing fields, outdated examples, and
undocumented validation rules have caused confusion for external
integrators.

Perform a full review of API documentation against the current
implementation. Update request/response examples and consider
introducing automated schema validation to reduce future drift.

## Issue 52 --- High CPU usage caused by inefficient notification queries

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-26
-   **Due date:** 2026-05-01

**Description:**\
Production monitoring indicates elevated CPU usage on application
servers during notification processing peaks. Database profiling
suggests that notification queries perform repeated full-table scans
when handling large user segments.

This has begun affecting response times during busy periods.

Optimize notification queries, add missing indexes where appropriate,
and review batching strategy to reduce server load.

## Issue 53 --- Inconsistent sorting behavior in admin user list

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Normal
-   **Assignee:** Maria Laine
-   **Start date:** 2026-04-27
-   **Due date:** 2026-05-02

**Description:**\
The admin user management table shows inconsistent sorting behavior
across columns. For example, sorting by "Last login" works correctly for
the first page of results but becomes unstable when navigating between
pages. Sorting by email is also case-sensitive, leading to unexpected
ordering (uppercase emails appearing separately from lowercase
equivalents).

This suggests that sorting is partially handled on the frontend while
pagination is handled on the backend, leading to mismatched ordering
logic.

Standardize sorting at the database query level to ensure consistent
results across all pages and filters.

## Issue 54 --- Exported CSV reports truncate long text fields

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-04-28
-   **Due date:** 2026-05-04

**Description:**\
When exporting reports to CSV, long text fields such as issue
descriptions, comments, and audit logs are being truncated without
warning. This leads to loss of critical information in exported
datasets, especially for compliance and auditing use cases.

The truncation appears to occur either due to backend serialization
limits or spreadsheet encoding constraints.

Ensure full field export without truncation, properly escape multiline
content, and validate compatibility with common spreadsheet tools.

## Issue 55 --- Webhook delivery lacks retry visibility in UI

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-04-29
-   **Due date:** 2026-05-15

**Description:**\
While webhook retries are implemented in the backend, there is currently
no way for users or administrators to view retry attempts, failure
reasons, or delivery history in the UI.

This makes debugging integration issues extremely difficult for external
clients.

Add a webhook monitoring dashboard that shows delivery attempts,
response codes, retry counts, and failure logs. Include filtering by
endpoint and time range.

## Issue 56 --- Slow performance on project overview page with large datasets

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-04-30
-   **Due date:** 2026-05-06

**Description:**\
The project overview page experiences significant slowdowns when
projects contain a large number of issues (500+). Rendering becomes
sluggish, and API response times increase noticeably.

Initial profiling suggests inefficient aggregation queries and excessive
frontend rendering of non-paginated data.

Optimize backend queries, introduce pagination or lazy loading for issue
lists, and consider caching summary metrics.

## Issue 57 --- Missing validation for email format in user invitation flow

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Sanna Lehto
-   **Start date:** 2026-05-01
-   **Due date:** 2026-05-03

**Description:**\
The user invitation form allows submission of invalid email formats
(e.g., missing domain or malformed addresses). In some cases,
invitations are still processed and sent to incorrect endpoints,
resulting in delivery failures or bounced emails.

Add proper client-side and server-side validation for email format and
ensure invalid inputs are rejected before processing.

## Issue 58 --- Add bulk issue editing capability in issue tracker

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** High
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-05-02
-   **Due date:** 2026-05-20

**Description:**\
Currently, administrators and project managers must update issues
individually, which is inefficient when handling large backlogs or
performing maintenance tasks.

Implement bulk editing functionality that allows updating multiple
issues simultaneously (e.g., changing status, assignee, priority, or
category).

Ensure proper permission checks, clear UI feedback, and safeguards to
prevent accidental large-scale modifications.

## Issue 59 --- Intermittent failure in password strength meter

-   **Tracker:** Bug
-   **Status:** Feedback
-   **Priority:** Low
-   **Assignee:** Laura Niemi
-   **Start date:** 2026-05-03
-   **Due date:** 2026-05-07

**Description:**\
The password strength meter in the registration form occasionally fails
to update in real time, especially when users type quickly or use
browser autofill. This results in outdated strength indicators being
displayed until the field loses focus.

The issue appears to be related to debounce timing and event handling
inconsistencies across browsers.

Improve event handling logic to ensure consistent real-time feedback.

## Issue 60 --- API rate limiting error messages are unclear

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** Normal
-   **Assignee:** Pekka Salonen
-   **Start date:** 2026-05-04
-   **Due date:** 2026-05-08

**Description:**\
When API rate limits are exceeded, the system returns generic error
responses that do not clearly explain the limit, reset time, or allowed
quota. This makes it difficult for API consumers to adjust their request
behavior.

Enhance rate limit responses to include structured metadata such as
remaining quota, retry-after headers, and human-readable explanations.

## Issue 61 --- Add configurable retention policy for logs

-   **Tracker:** Feature
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Antti Virtanen
-   **Start date:** 2026-05-05
-   **Due date:** 2026-05-25

**Description:**\
System logs currently accumulate indefinitely, leading to increased
storage costs and slower log queries over time. There is no mechanism
for automatic cleanup or archival.

Introduce configurable retention policies allowing administrators to
define how long logs are stored before deletion or archival. Include
support for exporting logs to external storage systems.

## Issue 62 --- Notification preferences reset after profile update

-   **Tracker:** Bug
-   **Status:** Confirmed
-   **Priority:** High
-   **Assignee:** Maria Laine
-   **Start date:** 2026-05-06
-   **Due date:** 2026-05-10

**Description:**\
Users report that their notification preferences (email, SMS, in-app)
are occasionally reset to default values after updating unrelated
profile fields such as name or password.

This suggests that the profile update endpoint may be overwriting
preference fields unintentionally or failing to merge partial updates
correctly.

Investigate request payload handling and ensure partial updates do not
overwrite unrelated user settings.

## Issue 63 --- Improve caching strategy for dashboard widgets

-   **Tracker:** Task
-   **Status:** In Progress
-   **Priority:** Normal
-   **Assignee:** Olli Heikkinen
-   **Start date:** 2026-05-07
-   **Due date:** 2026-05-22

**Description:**\
Dashboard widgets currently rely on a simplistic caching mechanism that
does not account for user-specific data freshness requirements. This
leads to either stale data being shown or excessive cache invalidation
causing performance degradation.

Redesign caching strategy to balance performance and freshness. Consider
per-widget caching rules and user-scoped cache keys.

## Issue 64 --- Incorrect pagination count in search results

-   **Tracker:** Bug
-   **Status:** New
-   **Priority:** Normal
-   **Assignee:** Jussi Korhonen
-   **Start date:** 2026-05-08
-   **Due date:** 2026-05-12

**Description:**\
The search results page displays incorrect total result counts when
filters are applied. In some cases, the UI shows more pages than
actually exist, leading to empty result pages when users navigate to the
end of the pagination.

This is likely caused by a mismatch between filtered query counts and
paginated result sets returned by the API.

Ensure that count queries and data queries use identical filtering
logic.

------------------------------------------------------------------------

## Notes for Redmine setup

-   Create the project and configure the trackers, statuses, and
    priorities before importing or entering issues.
-   Ensure the listed assignees exist as Redmine users and are members
    of the project.
-   Status names and tracker names must match the target Redmine
    instance configuration.
-   Dates are fictional sample dates and can be adjusted to fit your
    test environment.
-   The issue numbers in this document are reference numbers for this
    example dataset, not actual Redmine issue IDs.
