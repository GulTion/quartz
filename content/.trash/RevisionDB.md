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
  subject:
    input: select
    accessorKey: subject
    key: subject
    id: subject
    label: subject
    position: 5
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
      - { label: "C", value: "C", color: "hsl(300, 95%, 90%)"}
      - { label: "FULL", value: "FULL", color: "hsl(302, 95%, 90%)"}
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
    position: 7
    skipPersist: false
    isHidden: false
    sortIndex: 1
    width: 113
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
  type:
    input: select
    accessorKey: type
    key: type
    id: type
    label: type
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 185
    isSorted: false
    isSortedDesc: true
    options:
      - { label: "zealWorkBook", value: "zealWorkBook", color: "hsl(3, 95%, 90%)"}
      - { label: "single", value: "single", color: "hsl(38, 95%, 90%)"}
      - { label: "folder", value: "folder", color: "hsl(236,100%,85%)"}
      - { label: "ZealTS", value: "ZealTS", color: "hsl(189, 95%, 90%)"}
      - { label: "MadeEasyTS", value: "MadeEasyTS", color: "hsl(138, 95%, 90%)"}
      - { label: "GOTS", value: "GOTS", color: "hsl(2, 95%, 90%)"}
      - { label: "MicroNotes", value: "MicroNotes", color: "hsl(82, 95%, 90%)"}
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
  syllabus:
    input: text
    accessorKey: syllabus
    key: syllabus
    id: syllabus
    label: syllabus
    position: 8
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 354
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      wrap_content: true
      content_alignment: text-align-left
      content_vertical_alignment: align-top
  completed:
    input: checkbox
    accessorKey: completed
    key: completed
    id: completed
    label: completed
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: -2
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  subType:
    input: select
    accessorKey: subType
    key: subType
    id: subType
    label: subType
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "topicWise", value: "topicWise", color: "hsl(259, 95%, 90%)"}
      - { label: "mock", value: "mock", color: "hsl(98, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  atQ:
    input: number
    accessorKey: atQ
    key: atQ
    id: atQ
    label: atQ
    position: 2
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
  src:
    input: text
    accessorKey: src
    key: src
    id: src
    label: src
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