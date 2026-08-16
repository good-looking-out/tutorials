# How to Group and Ungroup Layers in Shred Scopes

Grouping combines related template layers into an organized unit for selection and coordinated canvas work. The individual elements remain editable, retain their own styles and telemetry mappings, and can be separated again with "Ungroup."

Use groups for components that should stay together, such as a speed value, its unit label, a gauge, and their shared background.

## Open a custom template

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and open the template in the Template Editor.

Create a custom copy with "Template" > "Save As New" when editing a built-in design.

## Prepare the layers

Before grouping:

- Give each layer a descriptive name.
- Put the elements in the intended front-to-back order.
- Confirm that the layers belong to the same logical component.
- Unlock any layer that must be selected or repositioned.

Grouping does not correct an incorrect stack automatically. A background placed in front of text can still cover it after both are grouped.

## Select the layers

Select the first layer on the canvas or in the layer list, then hold Shift while selecting the other required layers.

The multi-selection should contain only the intended elements. If an unrelated background or decoration is selected, clear the selection and try again.

Command+A on macOS or Control+A on Windows and Linux selects all editable layers. Use that shortcut only when the entire template should become one group.

## Create the group

With two or more layers selected:

1. Select "Group" above the layer list or use the corresponding canvas action.
2. Complete the "Create Group" step if Studio asks for a group name.
3. Enter a descriptive name such as "Speed gauge" or "Altitude readout."
4. Confirm the group.

Command+G on macOS or Control+G on Windows and Linux provides the keyboard shortcut.

The new group appears in the layer list with an expand or collapse control.

## Work with the complete group

Select the group when all of its children should be treated as one component. Depending on the active canvas operation, the group can be moved or transformed as a coordinated selection.

Grouping is useful for:

- Moving a complete gauge without leaving its label behind
- Repositioning a value, unit, and background together
- Hiding a complete component temporarily
- Locking a finished component against canvas changes
- Copying a complete component for reuse
- Keeping a long layer list organized

A group does not turn animated layers into static artwork. Data text, telemetry graphics, and data ticks continue to respond to the active source.

## Edit a child layer inside the group

1. Expand the group with its disclosure control.
2. Select the child layer by name or on the canvas.
3. Change its geometry, style, text, or telemetry controls.
4. Preview the group at several timeline positions.

Editing a child affects only that element. Select the group again before attempting a coordinated move.

## Reorder grouped layers

The child order inside a group controls how those children overlap. Move a child forward or backward within the group to correct local stacking.

The group's top-level position controls how the complete component overlaps layers outside it. Move the group itself when the entire component should go behind or in front of another top-level element.

## Copy or duplicate a group

Select the group and use its copy control or the normal copy and paste shortcuts. Paste it at the required top-level position.

A copied group preserves its internal arrangement. Rename the new group and any child layers that would otherwise be difficult to distinguish from the original.

Move the copy immediately after pasting because it can initially overlap the original.

## Ungroup layers

Use "Ungroup" when the elements need separate top-level editing:

1. Select the group or its grouped selection.
2. Choose "Ungroup."
3. Confirm that the former children now appear individually in the layer list.
4. Review their stack order and canvas positions.

Command+Shift+G on macOS or Control+Shift+G on Windows and Linux provides the keyboard shortcut.

Ungrouping removes the organizational container. It should not be confused with deleting the group.

## Avoid deleting the group by mistake

"Delete group and layers" removes every child along with the group. Use "Ungroup" if the elements must remain.

If a group is deleted unintentionally, use Command+Z or Control+Z immediately in the active template tab and verify that all of its children return.

## Review and save

After grouping or ungrouping:

- Play the telemetry preview.
- Check front-to-back order inside and outside the group.
- Confirm that locked or hidden state is intentional.
- Test a group move and undo it if the result was only a check.
- Save the custom template.

The layout now uses groups to keep related telemetry elements organized while preserving individual layer editability.
