# How to Add a Distance Traveled Overlay to GoPro Video

Shred Scopes can display cumulative distance from a GoPro GPS track as animated text, a gauge, or another telemetry graphic. The value increases as the playhead advances through valid recorded positions.

A distance overlay can describe the full recording or reset to zero at the beginning of a selected export range.

## Before starting

Use an original GoPro file containing valid GPS positions, or saved telemetry extracted from that file. Distance traveled cannot be calculated from a source that lacks a usable GPS path.

Decide whether the result should represent:

- Distance from the beginning of the complete recording
- Distance from the in point of a selected segment

That choice determines whether the telemetry graphics should be rebuilt from the active range.

## 1. Load the source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose "Choose Clip" for the original local file or "Choose Metadata from Account" for a saved extraction. Wait for Studio to prepare the telemetry and confirm that "Distance traveled" is available.

## 2. Choose a distance template

At "Choose Template," select a distance design. Built-in choices include imperial and metric variants in collections such as:

- Black Diamond Distance
- Flagship Distance or Flagship Distance Text
- Swell Distance or a Swell Distance Text layout
- Trailhead Distance or Trailhead Distance Text

Some multi-value templates also include distance alongside speed, altitude, or heading.

Choose the unit variant closest to the intended output, then open it in the Template Editor.

## 3. Confirm the distance stream

Select the data-text, data-graphic, or data-ticks layer that shows distance. In its input controls, confirm that "Stream" is set to "Distance traveled."

Distance traveled is cumulative. At each frame, it represents the route distance accumulated from the start of the active session or rebuilt range through that frame. It is not the straight-line distance between the start and current positions.

## 4. Choose the display unit

Distance uses meters before conversion. Use "Convert" to select:

- Feet
- Yards
- Miles
- Kilometers
- No conversion, which keeps meters

Choose a unit appropriate to the scale of the activity. Feet or meters can make a short run readable, while miles or kilometers are clearer for a long route.

Update any static unit label and set a suitable number of decimal places. A long-distance display may need one or two decimal places, while a short-distance display may be easier to read as a whole number of feet or meters.

## 5. Reset distance at a selected in point

By default, cumulative distance begins at the start of the active telemetry session. To make a selected video segment begin at zero:

1. Set the timeline in point.
2. Set the timeline out point.
3. Enable "Rebuild data graphics from range."
4. Wait for the range-dependent telemetry graphics to update.
5. Move the playhead to the new first frame and confirm that distance begins at zero.

Rebuilding discards telemetry before the in point and after the out point for range-dependent graphics. It also resets cumulative values such as distance to the selected beginning.

Choose the final range before setting precision or a fixed gauge scale because the total distance can change substantially after rebuilding.

## 6. Configure a distance gauge

If the template includes a gauge or ticks, choose how the cumulative distance should map to it.

Use:

- "fit data min/max" to make the recorded range fill the graphic
- "fixed range" to use an explicit start and end, such as 0–10 km

A fitted range emphasizes progress through one source. A fixed range is useful when several clips must use the same visual scale.

Keep the numeric readout, gauge, and ticks in the same unit. If the text is converted to miles while the ticks remain in meters, the display will not agree.

## 7. Preview the complete progression

Play the preview and check:

- The first frame of the active range
- Several intermediate route positions
- Stationary sections
- The final total

Distance should remain cumulative rather than dropping when the camera stops or changes direction. GPS gaps or position jumps can affect the total, so compare unexpected changes with the route and speed behavior.

## 8. Save and export

If the built-in design was modified, choose "Template" > "Save As New."

For a separate distance overlay, select the required export format in the Template Editor and choose "Export." Keep the tab open and visible through completion.

For a finished video, select "Composite Mode," position the overlay over the original footage, and export with Source Composite. Confirm that the same in and out points used to rebuild the distance are active for the final export.

## If the value is missing or begins at the wrong point

Check that:

- The source contains a valid GPS path.
- The layer is mapped to "Distance traveled."
- The correct saved telemetry record is loaded.
- "Rebuild data graphics from range" was enabled after setting the final in and out points.
- All related layers use the same unit conversion.
- The numeric precision is sufficient to show short-distance changes.

The completed overlay now shows cumulative route distance from the intended start point in the selected unit.
