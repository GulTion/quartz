---
database-plugin: basic
type: DataBase
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
    isSorted: false
    isSortedDesc: false
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      content_alignment: text-align-left
  startQ:
    input: number
    accessorKey: startQ
    key: startQ
    id: startQ
    label: startQ
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 70
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  endQ:
    input: number
    accessorKey: endQ
    key: endQ
    id: endQ
    label: endQ
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 52
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  totalQ:
    input: formula
    accessorKey: totalQ
    key: totalQ
    id: totalQ
    label: totalQ
    position: 7
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
      formula_query: ${parseInt(row.endQ-row.startQ+1)}
  atQ:
    input: number
    accessorKey: atQ
    key: atQ
    id: atQ
    label: atQ
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 18
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  subject:
    input: select
    accessorKey: subject
    key: subject
    id: subject
    label: subject
    position: 8
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "TOC", value: "TOC", color: "hsl(174, 95%, 90%)"}
      - { label: "CN", value: "CN", color: "hsl(141, 95%, 90%)"}
      - { label: "DM", value: "DM", color: "hsl(10, 95%, 90%)"}
      - { label: "OS", value: "OS", color: "hsl(300, 95%, 90%)"}
      - { label: "MATH", value: "MATH", color: "hsl(27, 95%, 90%)"}
      - { label: "COA", value: "COA", color: "hsl(38, 95%, 90%)"}
      - { label: "DBMS", value: "DBMS", color: "hsl(127, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  last_time:
    input: calendar
    accessorKey: last_time
    key: last_time
    id: last_time
    label: last_time
    position: 10
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
  repeation:
    input: number
    accessorKey: repeation
    key: repeation
    id: repeation
    label: repeation
    position: 9
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
  complete_till:
    input: formula
    accessorKey: complete_till
    key: complete_till
    id: complete_till
    label: complete_till
    position: 4
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
      formula_query: "${Math.round(100-(row.endQ - row.atQ)*100/row.totalQ)+\"%\"}"
  next_time:
    input: formula
    accessorKey: next_time
    key: next_time
    id: next_time
    label: next_time
    position: 11
    skipPersist: false
    isHidden: false
    sortIndex: 2
    isSorted: true
    isSortedDesc: false
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      formula_query: "${row.last_time.plus({days: row.repeation}).toFormat(\"y-LL-d\")}"
  type:
    input: select
    accessorKey: type
    key: type
    id: type
    label: type
    position: 2
    skipPersist: false
    isHidden: false
    sortIndex: 1
    width: 150
    isSorted: true
    isSortedDesc: true
    options:
      - { label: "zealWorkBook", value: "zealWorkBook", color: "hsl(3, 95%, 90%)"}
      - { label: "single", value: "single", color: "hsl(38, 95%, 90%)"}
      - { label: "folder", value: "folder", color: "hsl(236,100%,85%)"}
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
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /templates
  current_row_template: 
  pagination_size: 20
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