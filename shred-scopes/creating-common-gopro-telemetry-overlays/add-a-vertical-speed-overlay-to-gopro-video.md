# How to Add a Vertical Speed Overlay to GoPro Video

Shred Scopes can display the rate at which GoPro GPS altitude is increasing or decreasing. Positive vertical speed indicates climbing, while negative vertical speed indicates descending.

Vertical speed is different from altitude: altitude shows the current elevation, while vertical speed shows how quickly that elevation is changing.

## Before starting

Use an original GoPro clip with usable GPS altitude data, or saved telemetry extracted from that clip. A source without reliable altitude samples cannot provide meaningful vertical speed.

Decide whether the display should use meters per second, feet per minute, or another supported rate unit.

## 1. Load the telemetry

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio."

Choose an original local file or saved telemetry. Wait until Studio prepares the source and confirm that "Vertical speed" appears in the available stream list.

## 2. Choose a vertical-speed template

At "Choose Template," select an imperial or metric vertical-speed design. Choices are available in collections such as:

- Black Diamond Vertical Speed
- Flagship Vert Speed or Flagship Vertical Speed Text
- Swell Vertical Speed or a Swell Vertical Speed Text layout
- Trailhead Vertical Speed or Trailhead Vertical Speed Text

Choose an imperial version for feet-based output or a metric version for metric output.

## 3. Confirm the stream and sign

Select the data-text, data-graphic, or data-ticks layer that shows climbing and descending rate. Confirm that "Stream" is set to "Vertical speed."

The sign has a defined meaning:

- Positive values indicate climbing.
- Negative values indicate descending.
- Values near zero indicate little altitude change.

Keep numeric text, gauge direction, positive and negative colors, and labels consistent with this meaning.

## 4. Choose a vertical-speed unit

Vertical speed uses meters per second before conversion. Supported conversions include:

- Feet per minute
- Miles per hour
- Kilometers per hour
- Knots
- Other compatible speed or pace conversions

Feet per minute is often the clearest imperial unit for climbing and descending. Meters per second provides a direct metric rate.

Update any static suffix or label when changing units. Choose the conversion before setting a fixed range, clamp, or deadband because those values use the converted unit.

## 5. Center the range on zero

Use a signed range so climbs and descents appear on opposite sides of a neutral point.

Useful mappings are:

- "fit max absolute" for equal positive and negative limits based on the source
- "fixed range" for a consistent scale across multiple clips

An ordinary min/max fit can move the zero position when the largest climb and descent rates differ. A symmetric range keeps level movement centered.

Use "Clamp values" only when an isolated GPS spike makes the visual range unusable. Set the limits in the selected converted unit.

## 6. Reduce noise around level travel

Vertical speed derived from GPS altitude can fluctuate around zero even when the path is nearly level.

Use moderate "Smoothing" to reduce rapid changes. Check short climbs and descents afterward because heavy smoothing can conceal them.

Use "Deadband" centered on zero when small fluctuations make the indicator jitter. The deadband holds values inside its window at zero while leaving larger climbs and descents unchanged.

Do not use a wide deadband that removes legitimate low-rate elevation changes.

## 7. Preview the full behavior

Inspect:

- A level section
- A sustained climb
- A sustained descent
- The strongest positive and negative values
- Stops and low-motion sections

Confirm that the value's sign agrees with altitude movement. If altitude is increasing while the vertical-speed graphic indicates descending, inspect stream mapping, graphic direction, and range settings.

An abrupt one-frame change can reflect GPS noise rather than an actual vertical movement. Review the surrounding altitude and motion before treating it as a meaningful event.

## 8. Save and export

Use "Template" > "Save As New" to retain a customized built-in design.

Export the template by itself for use in another video editor, or choose "Composite Mode" to place it over the original footage and render a finished Source Composite video.

Keep the Studio tab open and visible while the export runs.

## If vertical speed is unavailable or unreadable

Check that:

- The source contains usable GPS altitude data.
- The layer uses "Vertical speed" rather than altitude.
- The unit suffix matches the selected conversion.
- The mapping range includes both positive and negative movement.
- Smoothing, deadband, or clamping is not hiding valid changes.

The completed overlay now distinguishes climbing from descending with a signed rate, appropriate unit, and neutral-centered scale.
