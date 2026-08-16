# How to Add an Altitude Overlay to GoPro Video

Shred Scopes can display the elevation recorded by a GoPro as animated text, a gauge, or another telemetry graphic. An altitude overlay can be exported separately or rendered over the original video with Source Composite.

The source must contain usable GPS altitude data.

## Before starting

Prepare an original GoPro clip recorded with GPS enabled and a usable satellite lock, or a saved telemetry extraction from that clip.

Altitude in Studio represents the values recorded by the GoPro GPS system. It should not be assumed to match a separately calibrated barometric instrument, survey elevation, or map elevation at every frame.

## 1. Load the GoPro telemetry

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose the original video with "Choose Clip," or select saved telemetry with "Choose Metadata from Account." Wait until the source is ready and confirm that "Altitude" appears among its available streams.

## 2. Choose an altitude template

At "Choose Template," select an altitude design. Built-in imperial and metric choices are available in collections such as:

- Black Diamond Altitude
- Flagship Altitude or Flagship Altitude Text
- Swell Altitude or a Swell Altitude Text layout
- Trailhead Altitude or Trailhead Altitude Text

Choose the metric variant for meters or the imperial variant for feet. A built-in template can be opened as-is and saved as a separate custom copy after changes.

## 3. Confirm the altitude mapping

In the Template Editor, select the data-text or data-graphic layer that displays elevation. Open its data controls and confirm that "Stream" is set to "Altitude."

If several layers participate in the design, check each relevant element:

- Numeric altitude text
- Gauge or progress graphic
- Data-driven ticks
- Static unit label

The data-driven elements should use the same altitude stream and compatible ranges.

## 4. Choose meters or feet

Altitude uses meters as its unconverted value. Use "Convert" to choose the required display unit.

Available distance conversions include:

- Feet
- Yards
- Miles
- Kilometers

Meters or feet are normally the clearest choices for an elevation overlay. Update any static unit label so it matches the selected conversion.

Set the displayed decimal precision after choosing the unit. A whole number is often readable for meters or feet, while excessive decimals can imply more precision than the recorded GPS supports.

## 5. Choose an altitude range

For a gauge, profile, or moving indicator, decide how the recorded values should fit the graphic.

Use:

- "fit data min/max" when the gauge should adapt to the lowest and highest altitude in the active data
- "fixed range" when multiple videos should use a consistent elevation scale

An automatic range emphasizes the change within one clip, even when the total change is small. A fixed range makes separate clips easier to compare but can reduce visible movement when the chosen span is large.

If an isolated GPS value produces an unrealistic scale, use "Clamp values" cautiously. Set clamp values in the converted unit currently selected for the layer. Clamping changes only that layer's input and does not repair the extracted telemetry.

## 6. Preview the altitude behavior

Play the preview and inspect:

- The start and end of the clip
- The lowest recorded point
- The highest recorded point
- Climbs and descents
- Stationary or low-motion sections

Confirm that the numeric text, ticks, and graphic position agree. Watch for abrupt isolated jumps that may indicate weak GPS coverage rather than actual elevation change.

Altitude and vertical speed are different measurements. Altitude shows elevation at the current frame; vertical speed shows how quickly elevation is changing.

## 7. Adjust appearance and placement

Move or scale the complete altitude design so it remains legible without covering important action.

Common changes include:

- Increasing text contrast
- Adding a background or outline
- Reducing unnecessary decimal places
- Changing colors and opacity
- Resizing the canvas for a compact overlay

Preview the graphic against both light and dark source frames when it will be composited over the original video.

## 8. Save and export

Use "Template" > "Save As New" to retain a modified built-in design.

For a standalone overlay, choose a transparency-capable MOV or WebM when supported by the finishing editor, or use a keyed-background MP4 when chroma keying is planned. Select "Export" and leave the browser tab open and visible until the render finishes.

For a finished video, select "Composite Mode," position the altitude overlay over the original footage, and export the Source Composite file.

## If altitude is unavailable or unstable

Check that:

- The source is the original GoPro file.
- The camera and recording mode support GPS data.
- GPS was enabled and had a usable satellite lock.
- The correct telemetry record is active.
- The layer uses "Altitude" rather than a different height-related stream.
- Smoothing, clamping, or range settings are not concealing valid movement.

The completed overlay now displays GoPro-recorded elevation in the selected unit across the active video range.
