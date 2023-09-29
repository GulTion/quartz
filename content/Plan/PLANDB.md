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
    position: 1
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  type:
    input: select
    accessorKey: type
    key: type
    id: type
    label: type
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 147
    options:
      - { label: "zealWorkBook", value: "zealWorkBook", color: "hsl(3, 95%, 90%)"}
      - { label: "zealTS", value: "zealTS", color: "hsl(48, 95%, 90%)"}
      - { label: "MadeEasyTS", value: "MadeEasyTS", color: "hsl(353, 95%, 90%)"}
      - { label: "GOTS", value: "GOTS", color: "hsl(53, 95%, 90%)"}
      - { label: "PYQ", value: "PYQ", color: "hsl(265, 95%, 90%)"}
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
  Repetation:
    input: number
    accessorKey: Repetation
    key: Repetation
    id: Repetation
    label: Repetation
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 91
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
    label: Last_Time
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
  Next_Time:
    input: formula
    accessorKey: Next_Time
    key: Next_Time
    id: Next_Time
    label: Next_Time
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: 1
    width: -2
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
      formula_query: "${row.Last_Time.plus({days: row.Repetation}).toFormat(\"y-LL-d TT\")}"
      wrap_content: true
  __tags__:
    key: __tags__
    id: __tags__
    input: metadata_tags
    label: File Tags
    accessorKey: __tags__
    isMetadata: true
    isDragDisabled: false
    skipPersist: false
    csvCandidate: false
    position: 0
    isHidden: true
    sortIndex: -1
    width: -18
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  path:
    input: text
    accessorKey: path
    key: path
    id: path
    label: path
    position: 100
    skipPersist: false
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
      wrap_content: false
  atQ/P:
    input: text
    accessorKey: atQ/P
    key: atQ/P
    id: atQ/P
    label: atQ/P
    position: 100
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
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: false
  group_folder_column: 
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: true
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /
  current_row_template: 
  pagination_size: 200
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