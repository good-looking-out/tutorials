# How to Duplicate and Lock Template Layers

Duplicating creates an independent copy of a selected layer or group. Locking protects a finished selection from accidental direct canvas movement while other parts of the template are being arranged.

These actions are useful when building repeated labels, matching decorations, parallel gauges, or stable background structures.

## Open the Template Editor

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the required template.

Use "Template" > "Save As New" when changing a built-in template so the revised version can be retained as a custom design.

## Duplicate one layer

1. Select the layer on the canvas or in the "Layers" list.
2. Press Command+D on macOS or Control+D on Windows and Linux.
3. Find the new entry in the layer list.
4. Rename the copy.
5. Move it away from the original.

A duplicate can begin directly over or near its source. If the canvas appears unchanged, check the layer list before repeating the command.

## Copy and paste at a chosen stack position

Use copy and paste when the new layer should be inserted at a specific point:

1. Select the source layer.
2. Use its copy control, or press Command+C or Control+C.
3. Find the intended position in the layer list.
4. Select "Paste here."

The pasted layer begins at that draw position. Use "Clear copied layer" when the held copy is no longer needed.

Command+V on macOS or Control+V on Windows and Linux also pastes the copied selection.

## Understand duplicate independence

The copy has its own geometry, style, text, and telemetry settings. Changing those properties on the duplicate does not automatically make the same edit to the source layer.

However, both layers can still use the same template constant. If the original and copy remain linked to a shared color or font constant, changing that constant updates both. Replace the constant with a literal value on one layer when they should be styled independently.

## Duplicate a group

Select a group when an entire assembled component should be reused. Duplicate or copy and paste it as a unit, then:

- Rename the copied group.
- Rename similar child layers where useful.
- Move the copy away from the source.
- Change telemetry mappings or labels that should differ.
- Check the new group's stack position.

This is faster and more consistent than rebuilding a multi-layer gauge one element at a time.

## Lock a finished layer

Select the layer and use its lock control in the layer list. The icon changes to indicate the locked state.

Other methods include:

- Press L while the layer is selected.

Locking is intended to prevent accidental canvas manipulation. It does not hide the layer or remove it from the export. The layer remains part of the template and can still be selected from the layer list for available non-canvas controls.

## Unlock for revisions

Select the locked layer from the list, then use the unlock icon or press L again.

Unlock before attempting to drag, resize, rotate, or nudge it on the canvas. Lock it again after the revision if it should remain protected.

## Lock backgrounds and framing elements

A practical editing sequence is:

1. Position the full-canvas background.
2. Put it at the back of the stack.
3. Lock it.
4. Position decorative frames and lock them after approval.
5. Continue editing smaller text and telemetry layers above them.

This prevents a large background from being selected and moved while trying to edit a smaller overlapping element.

## Lock or duplicate multi-selections

Hold Shift to select several layers. Press L to change the lock state of the current canvas selection, or duplicate the selection with the standard shortcut when the complete set should be copied.

Grouping first can make repeated operations easier when the same elements will continue to act as one component.

## Resolve common problems

### A duplicate is not visible

Inspect the layer list. The copy may overlap the original exactly or may be hidden behind an opaque layer. Select it by name and move or bring it forward.

### A layer will not move

Check its lock icon and whether a parent group is locked. Unlock the relevant selection before using the canvas.

### Editing one copy changes another

Check whether both use the same color, font, number, or text constant. Assign a separate literal value or a different constant when independent styling is required.

### The wrong item was duplicated

Use Command+Z or Control+Z, clear the selection, select the intended layer from the list, and duplicate again.

## Save the result

Save the custom template after duplicated elements are renamed, positioned, and checked. Lock state and the duplicate's independent settings are retained with the template.

The layout now reuses repeated elements efficiently while protecting finished layers from accidental canvas changes.
