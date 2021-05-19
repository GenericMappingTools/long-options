# Long-options
Organization-wide repository of long-option selections for arguments,
directives, and modifiers.

# Repository structure
- `modules/` - contains a .json file for each GMT module. The JSON file for
each module contains the following name/value pairs:
  - "module_options": array of non-common options available to the module
    (e.g., `["A","E"]`).
  - "module_needs": array of required options ( e.g., `["R","J","A"]`).
  - "module_common": array of common options available to the module
    (e.g., `["R","J","V"]`).
  - "module_other": array of other input to the module (e.g., `["table"]` or
    `["preflight"]`).
  - one name/object pair for each non-common option that contains the following
    name/value pairs:
    - "long-option": string containing the proposed long-option for the
      non-common option (e,g, `"long-option": "annotation"`).
    - "directives": object containing name/value pairs for the short- and
      long-forms of each directive available to the option (e.g.,
      `"directives": {"i": "in", "o": "out"}`).
    - "modifiers": object containing name/value pairs for the short- and
      long-forms of each modifier available to the option (e.g.,
      `"modifiers": {"r": "rectangular", "u": "unit"}`).
    - "other-modules": array containing other modules that use the same or
      similar non-common options (e.g.,
      `"other-modules": ["blockmean","blockmode"]`).
- `common-options/` - contains a .json file for each letter used for common
options. Upper-case and lower-case common options for the same case-insensitive
letter are stored in the same JSON file (e.g., `B`,`bi`, and `bo` are all in
`common-options/b.json`). Each common option contains the same name/value pairs
as the non-common options:
    - "long-option": string containing the proposed long-option for the
      common option (e,g, `"long-option": "frame"`).
    - "directives": object containing name/value pairs for the short- and
      long-forms of each directive available to the option (e.g.,
      `"directives": {"i": "in", "o": "out"}`).
    - "modifiers": object containing name/value pairs for the short- and
      long-forms of each modifier available to the option (e.g.,
      `"modifiers": {"r": "rectangular", "u": "unit"}`).
    - "other-modules": array containing list of modules that can use the common
      option.
- `construct-dataframe.py` - a Python script that creates a pandas DataFrame from
the common-option and modules JSON files.
# Process for selecting long-options
1. Create a branch
2. Edit the .json file for the module in `modules/` to add the proposed
   long-format selections. See above for the structure of the files.
   If there are other modules listed under `other-modules`, it is
   recommended that you add the proposed long-option name(s) to those modules
   as well.
3. Submit a pull-request for review.
4. Wait for approval from at least one person with write access to the
   repository and for at least 48 hours before merging the pull request.