# Studio Interface Tour: Source, Template, Preview, Timeline, and Export

Studio is the authenticated Shred Scopes page used to load GoPro telemetry, edit templates, preview animation, arrange Source Composites, and export video. Its controls change as a project moves from source selection to the Template Editor or Source Compositor.

This tour identifies the major areas of the workspace and the role each one performs.

## Open Studio

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio" from the site navigation.

Use a current Chromium-based browser for the fullest editing and export support. Studio does not open on a phone or tablet.

## Startup source picker

When no project is active, Studio presents the source choices:

- "Choose Clip" selects an original local GoPro video.
- "Use Sample Clip" opens the included sample picker.
- "Choose Metadata from Account" loads an extraction saved to the account.

After a local file is selected, Studio prepares its telemetry. The next step is "Choose Template." Select a design to enter the Template Editor, or choose a different clip to return to the source picker.

## Template Editor overview

The Template Editor is used to build and export an individual telemetry overlay. It has four principal regions.

| Area | Purpose |
| --- | --- |
| Left sidebar | Source controls, overlay export settings, template constants, layers, and selected-layer controls |
| Top toolbar | Template tabs, new and change actions, mode switch, template menu, reset, and export |
| Canvas | The active template rendered at the current telemetry frame |
| Bottom bar | Status, zoom, preview playback, and the telemetry timeline |

### Left sidebar

The upper source section shows which telemetry is active and provides controls such as:

- "Choose Clip" or "Choose New Clip"
- "Use Sample Clip"
- "Change Source File"
- "Choose Metadata from Account"
- "Select Source Video" when telemetry is loaded without the original video

The export section contains the overlay format, export size, and applicable source-timecode option.

"Template Constants" contains shared color, font, number, or text values used by compatible layers. "Layers" shows the template stack and the controls for each selected element.

Expanding a layer reveals settings appropriate to its type. A data-text layer exposes telemetry and formatting controls, while a shape, image, tick, or data-graphic layer exposes a different set.

### Top toolbar

Template tabs appear across the top. Each tab is a separate working design with its own selection, unsaved state, and undo history.

The principal toolbar actions are:

- "+" opens another template in a new tab.
- "CHANGE TEMPLATE" replaces the active tab's template after unsaved work is resolved.
- "New" starts a blank template and requests a name and canvas size.
- "Resize" exposes handles for changing the template canvas.
- "Composite Mode" opens the Source Compositor with the current template.
- "Template" opens save, copy, frame, undo, redo, and shortcut actions as available.
- "Reset" returns Studio to its startup state after unsaved work is resolved.
- "Export" starts an overlay render using the sidebar settings.

For a built-in template, use "Save As New" to preserve a customized copy. "Save" applies to an existing custom template with unsaved changes.

### Canvas

The canvas displays the active template at the telemetry frame selected on the timeline. Supported layers can be selected, moved, resized, or rotated directly.

Right-clicking the canvas provides contextual actions for adding, copying, showing, hiding, arranging, centering, grouping, or deleting layers. When several layers overlap, "Select layer" identifies the element to edit.

Selection outlines and handles are editing aids and are not included in the clean export.

### Bottom bar and timeline

The bottom bar reports the current Studio status. It also contains:

- Preview zoom
- "Play preview" and "Pause preview"
- The telemetry timeline and playhead

Preview zoom changes only the on-screen view. It does not resize the template or video output.

Drag the playhead to inspect a specific time. Press Space to play or pause when the workspace has focus.

## Layers and selection controls

The layer list controls the template's visual stack. Common actions include:

- "Add Layer" to open the layer picker
- Plus buttons between layers to insert at a specific position
- Up and down controls to change stack order
- Eye controls to show or hide an element
- Lock controls to prevent or allow canvas movement
- Rename, copy, select, and delete controls
- Expand and collapse controls for groups

When multiple layers are selected, alignment, distribution, grouping, and ungrouping controls appear above the list.

## Source Compositor overview

Select "Composite Mode" or press `M` after loading an original video and a template. The Source Compositor arranges the source and one or more telemetry templates on the same output canvas.

Its main regions remain similar, but their purposes change:

| Area | Purpose |
| --- | --- |
| Left control panel | Output canvas, source and template placement, timeline range, compatibility, and encoding |
| Top toolbar | Return to Template Editor, shared history and shortcut actions, reset, and Source Composite export |
| Canvas | Source video and telemetry overlays rendered together |
| Bottom bar | Preview zoom, playback, playhead, and in and out points |

### Source controls

Source Composite can lock or unlock the video, fit it with "Cover" or "Contain," rotate it, and adjust its X, Y, and scale values. Alignment actions provide additional positioning control.

### Template-overlay controls

Select an overlay to change its position and scale. The controls also allow the template to be locked, duplicated, edited in a linked Template Editor tab, or removed from the composite. "Add Template" opens the picker for another overlay.

### Range and encoding controls

The Source Compositor includes:

- In and out points
- "Rebuild data graphics from range"
- Browser and encoder "Compatibility" results
- H.264 and HEVC/H.265 codec choices where supported
- Target bitrate
- Advanced encoding controls
- Resize sampling
- Source-timecode controls

The "Reset" button at the bottom of the control panel restores source and template framing. It is different from the top toolbar's "Reset," which returns the entire Studio page to its startup state.

## Moving between the two editing views

Use "Composite Mode" to move from Template Editor to Source Composite. Use "Template Editor Mode" to return. The `M` keyboard shortcut switches between them.

Returning to Template Editor Mode does not automatically clear the Source Composite arrangement. An overlay opened with "Edit Template" remains connected to the composite, allowing its internal design to be changed and previewed in context.

## Leaving the workspace safely

Before closing a template tab, resetting Studio, returning to media management, or leaving the page, review any unsaved indicator.

Use "Save" for an existing custom template and "Save As New" for a built-in template or new version. Studio displays a confirmation when an action could discard unresolved work.

The "Manage Media" area outside the editor provides access to imported telemetry, favorite and custom templates, image assets, and the export log. Use "Open Studio" there to return to the editing page.
