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
    position: 2
    isHidden: false
    sortIndex: -1
    width: 108
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
  subject:
    input: select
    key: subject
    accessorKey: subject
    label: Subject
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "APTI", value: "APTI", color: "hsl(346, 95%, 90%)"}
      - { label: "ALGO", value: "ALGO", color: "hsl(343, 95%, 90%)"}
      - { label: "CN", value: "CN", color: "hsl(54, 95%, 90%)"}
      - { label: "COA", value: "COA", color: "hsl(322, 95%, 90%)"}
      - { label: "OS", value: "OS", color: "hsl(258, 95%, 90%)"}
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
      formula_option_source: 
  Topic:
    input: tags
    accessorKey: Topic
    key: Topic
    id: Topic
    label: Topic
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 133
    options:
      - { label: "Data Link Layer", value: "Data Link Layer", color: "hsl(8, 95%, 90%)"}
      - { label: "Stack", value: "Stack", color: "hsl(285, 95%, 90%)"}
      - { label: "Recursion", value: "Recursion", color: "hsl(194, 95%, 90%)"}
      - { label: "Queue", value: "Queue", color: "hsl(275, 95%, 90%)"}
      - { label: "Linked List", value: "Linked List", color: "hsl(263, 95%, 90%)"}
      - { label: "Binary Tree", value: "Binary Tree", color: "hsl(208, 95%, 90%)"}
      - { label: "Binary Search Tree", value: "Binary Search Tree", color: "hsl(65, 95%, 90%)"}
      - { label: "Construction Of AVL Tree", value: "Construction Of AVL Tree", color: "hsl(334, 95%, 90%)"}
      - { label: "Number System", value: "Number System", color: "hsl(219, 95%, 90%)"}
      - { label: "Instruction Set Architecture", value: "Instruction Set Architecture", color: "hsl(313, 95%, 90%)"}
      - { label: "Addressing Mode", value: "Addressing Mode", color: "hsl(350, 95%, 90%)"}
      - { label: "Pipeline", value: "Pipeline", color: "hsl(327, 95%, 90%)"}
      - { label: "Process Syncronization", value: "Process Syncronization", color: "hsl(17, 95%, 90%)"}
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
      wrap_content: false
      content_alignment: text-align-center
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
    position: 6
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
      - { label: "PYQ", value: "PYQ", color: "hsl(242, 95%, 90%)"}
      - { label: "Zeal TS", value: "Zeal TS", color: "hsl(202, 95%, 90%)"}
      - { label: "Zeal WB", value: "Zeal WB", color: "hsl(222, 95%, 90%)"}
      - { label: "ME TS", value: "ME TS", color: "hsl(85, 95%, 90%)"}
      - { label: "GO TS", value: "GO TS", color: "hsl(28, 95%, 90%)"}
      - { label: "UaNotes", value: "UaNotes", color: "hsl(291, 95%, 90%)"}
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
  Last_Time:
    input: calendar_time
    accessorKey: Last_Time
    key: Last_Time
    id: Last_Time
    label: Last Time
    position: 8
    skipPersist: false
    isHidden: false
    sortIndex: -1
    isSorted: false
    isSortedDesc: true
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
    position: 9
    skipPersist: false
    isHidden: false
    sortIndex: 1
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
  Repetation:
    input: number
    accessorKey: Repetation
    key: Repetation
    id: Repetation
    label: Repetation
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
  ID:
    input: number
    accessorKey: ID
    key: ID
    id: ID
    label: ID
    position: 1
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 43
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Planner_Type:
    input: select
    accessorKey: Planner_Type
    key: Planner_Type
    id: Planner_Type
    label: Planner Type
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "TS Analysis", value: "TS Analysis", color: "hsl(331, 95%, 90%)"}
      - { label: "Revision", value: "Revision", color: "hsl(237, 95%, 90%)"}
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
  show_metadata_created: true
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /templates
  current_row_template: templates/Planner Template.md
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