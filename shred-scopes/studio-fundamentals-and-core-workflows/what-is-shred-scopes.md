# What Is Shred Scopes?

Shred Scopes is a browser-based application for turning telemetry recorded inside compatible GoPro video files into animated graphics. It can export those graphics as a standalone video overlay or render them directly over the original GoPro footage as a finished video.

The application's authenticated editing page is called "Studio." This is the workspace used for adding a speedometer, altitude graph, GPS route, distance counter, grade indicator, G-force meter, heading display, or other telemetry visualization to GoPro footage. The graphics are template-based and can be customized before export.

## What Shred Scopes does

A compatible GoPro file can contain an embedded telemetry track in addition to its video and audio tracks. GoPro stores this information in its GoPro Metadata Format, commonly abbreviated as GPMF.

Within the application, Studio reads the telemetry track locally in the browser and prepares its values for use in animated template layers. Depending on what the camera recorded, those values can include:

- Ground and three-dimensional speed
- Altitude and vertical speed
- Distance traveled
- GPS course and route
- Grade or slope
- Acceleration and G-force
- Camera-axis acceleration and rotation rate
- GPS date and time
- Elapsed time and detected airtime

The exact list available in Studio depends on the telemetry contained in the selected source file. A template that requires GPS data, for example, cannot display that data if the camera did not record it.

## The basic Shred Scopes workflow

A typical Shred Scopes session begins on the public website and continues in the authenticated Studio page:

1. Open [Shred Scopes](https://shredscopes.com/) in a supported desktop browser, sign in, and select "Studio" from the site navigation.
2. Select an original GoPro video, load telemetry previously saved to the account, or choose an included sample clip.
3. Wait for Studio to prepare the available telemetry.
4. Choose a built-in telemetry template or open a saved custom template.
5. Customize the template's layout, data mapping, units, text, colors, fonts, images, and other visual settings.
6. Preview the animation and inspect different points in the timeline.
7. Export a standalone telemetry overlay or switch to Source Composite to render the graphics over the original footage.

The Studio workspace uses the same telemetry-driven rendering system for its canvas preview and export. Previewing several points in the source is therefore an important way to check the values, ranges, placement, and legibility of an overlay before starting a video export.

## Source choices

The Studio page can begin with three types of source material.

### Original GoPro video

An original GoPro clip provides the most complete workflow. Studio can read its telemetry and, where available, use its video frames, audio, dimensions, frame rate, and source timecode.

The original file remains on the user's device. Telemetry extraction, preview, compositing, and export take place in the browser. Saving extracted telemetry to a Shred Scopes account is optional and does not upload the original source footage.

### Saved telemetry

Telemetry saved to an account can be loaded without repeating extraction from the source clip. It can drive a template preview and a standalone overlay export.

Saved telemetry does not include the original video's frames or audio. Studio requires the matching original GoPro file before it can create a Source Composite from saved telemetry.

### Included sample clip

An included sample clip can be used to learn the editor and test templates without supplying personal footage. Its telemetry, duration, aspect ratio, and motion apply only to that sample and should not be treated as representative of another GoPro recording.

## Template Editor and Source Composite

Within Studio, two related editing views are available.

### Template Editor

The Template Editor is used to create an individual telemetry graphic. A template is assembled from layers such as:

- Static and data-driven text
- Shapes and lines
- Images
- Linear and radial ticks
- Gauges, meters, charts, GPS paths, and other data graphics
- Other reusable templates

Layers can be added, removed, positioned, resized, reordered, grouped, styled, and connected to compatible telemetry streams. Unit conversion controls can display measurements in forms such as miles per hour, kilometers per hour, feet, meters, miles, or kilometers.

The Template Editor can export the overlay by itself. Transparency-capable choices include PNG-codec MOV, QuickTime Animation MOV, and supported WebM configurations. Shred Scopes can also create an H.264 MP4 over a solid color for a chroma-key workflow.

### Source Composite

Source Composite places one or more telemetry templates over the original GoPro video. Each overlay can be positioned and scaled independently, while the source footage can be fitted to the intended output dimensions.

This view exports a finished MP4 using H.264 or, when supported by the browser and downstream workflow, HEVC/H.265. Source Composite exports include the original source audio.

GoPro `.360` files can supply telemetry for template work, but their video cannot currently be previewed or rendered in Source Composite.

## Built-in and custom templates

Shred Scopes includes ready-made telemetry templates for common data such as speed, altitude, distance, GPS path, grade, acceleration, G-force, heading, and vertical speed. Many templates have separate imperial and metric versions.

Built-in templates can be used as supplied or opened as the starting point for a custom design. A custom template can change the selected data, units, layer arrangement, dimensions, colors, typography, and other settings. With full access, custom templates can be saved to the account and reused with later telemetry sources.

The current template catalog is available at [GoPro Telemetry Overlay Templates](https://shredscopes.com/gopro-telemetry-overlay-templates).

## Standard and Batch Mode

Standard mode handles one source at a time. It is the normal choice for creating a single overlay or finished video and for learning the editor.

Selecting two or more local GoPro clips can start Batch Mode. Batch Mode provides two output workflows:

- **Batch Template Export** applies one template to each source and exports the overlay outputs.
- **Batch Source Composite** places one or more templates over each source video and exports finished videos.

Batch exports run sequentially and track progress for each source. Batch Mode requires a Chromium-based desktop browser because the browser must receive permission to write multiple files to a selected output directory.

## Browser and device requirements

The Studio editor is designed for desktop computers. Phones and tablets can display public and account-management pages in Shred Scopes, but they cannot open the editing workspace.

A current Chromium-based desktop browser, such as Chrome, Edge, Brave, or Opera, provides the broadest support. Firefox and Safari have limitations affecting some preview, encoding, file-saving, and batch workflows.

Shred Scopes runs in the browser and does not require a separate desktop application installation. Video export can be demanding, so the Studio tab should remain open and visible until rendering finishes.

## Full-access features

The Studio page can be explored with its included sample material, but actions that create or retain output require full access. These actions include:

- Saving extracted telemetry to the account
- Uploading and using account image assets
- Saving new or changed custom templates
- Saving a still frame
- Exporting standard or batch video output

The current access state is shown inside Studio when one of these actions is selected.

## Summary

Shred Scopes combines three functions in one browser workflow: it reads telemetry from compatible GoPro footage, turns that data into customizable animated graphics, and exports either a separate overlay or a finished video containing the source footage. Studio is the authenticated page where the editing and export portions of that workflow take place.

The central distinction is the intended output. Use the Template Editor when the telemetry graphics will be added to footage in another video editor. Use Source Composite when the goal is to position the graphics over the original clip and export a finished MP4 directly from Shred Scopes.
