---

database-plugin: basic

---

```yaml:dbfolder
name: new database
description: new description
columns:
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 4
    isHidden: false
    sortIndex: -1
    width: 143
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      wrap_content: true
  __created__:
    key: __created__
    id: __created__
    input: metadata_time
    label: Created
    accessorKey: __created__
    isMetadata: true
    isDragDisabled: false
    skipPersist: false
    csvCandidate: true
    position: 1
    isHidden: true
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  __modified__:
    key: __modified__
    id: __modified__
    input: metadata_time
    label: Modified
    accessorKey: __modified__
    isMetadata: true
    isDragDisabled: false
    skipPersist: false
    csvCandidate: true
    position: 2
    isHidden: true
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  repetation:
    input: number
    accessorKey: repetation
    key: repetation
    id: repetation
    label: repetation
    position: 8
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 74
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Last_Time:
    input: calendar_time
    accessorKey: Last_Time
    key: Last_Time
    id: Last_Time
    label: Last Time
    position: 9
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 68
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Next_Time:
    input: formula
    accessorKey: Next_Time
    key: Next_Time
    id: Next_Time
    label: Next Time
    position: 10
    skipPersist: false
    isHidden: false
    sortIndex: 1
    width: 101
    isSorted: true
    isSortedDesc: false
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      formula_query: "${row.Last_Time.plus({days: row.repetation}).toFormat(\"y-LL-d TT\")}"
      wrap_content: true
  subject:
    input: select
    accessorKey: subject
    key: subject
    id: subject
    label: subject
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 55
    options:
      - { label: "CD", value: "CD", color: "hsl(58, 95%, 90%)"}
      - { label: "CN", value: "CN", color: "hsl(191, 95%, 90%)"}
      - { label: "OS", value: "OS", color: "hsl(305, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Note:
    input: text
    accessorKey: Note
    key: Note
    id: Note
    label: Note
    position: 11
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Source:
    input: select
    accessorKey: Source
    key: Source
    id: Source
    label: Source
    position: 7
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "ME SHORT NOTES", value: "ME SHORT NOTES", color: "hsl(206, 95%, 90%)"}
      - { label: "UaNotes", value: "UaNotes", color: "hsl(180, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      option_source: manual
      wrap_content: true
      content_alignment: text-align-left
  PID:
    input: number
    accessorKey: PID
    key: PID
    id: PID
    label: PID
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  type:
    input: select
    key: type
    accessorKey: type
    label: Type
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "Short Notes", value: "Short Notes", color: "hsl(261, 95%, 90%)"}
      - { label: "Full Notes", value: "Full Notes", color: "hsl(65, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      option_source: manual
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: false
  group_folder_column: 
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: true
  show_metadata_modified: true
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /templates
  current_row_template: templates/Note Template.md
  pagination_size: 10
  font_size: 16
  enable_js_formulas: false
  formula_folder_path: /
  inline_default: false
  inline_new_position: last_field
  date_format: yyyy-MM-dd
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
  implementation: default
filters:
  enabled: false
  conditions:
```