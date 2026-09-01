# What’s New in Ableton Live 12.2

Ableton Live 12.2 added a faster way to commit material to audio, new chord-generation and sound-design tools, and refinements to the Browser. This guide covers the Live 12.2 feature set demonstrated in Ableton’s June 2025 overview video. Open [Ableton Live](https://www.ableton.com/en/live/) and a Set containing a few MIDI or audio clips before following along.

Live 12 has continued to receive updates since version 12.2. The controls described here are current Live 12 concepts, but features introduced in later versions are outside this article’s scope. Check Ableton’s [Live 12 release notes](https://www.ableton.com/en/release-notes/live-12/) for the changes in the installed version.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/E4e5-LhpkGg?rel=0"
    title="What's new in Ableton Live 12.2? Feature Overview"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Check the version and feature availability

The source video was published on June 11, 2025, alongside Live 12.2. Confirm that the installed version is 12.2 or later before looking for its new controls. Live 12.2 was released as a free update for Live 12 users, but some devices remain edition-dependent.

The following Live 12.2 features are available in the relevant current editions:

- **Bounce to New Track**, the redesigned **Auto Filter**, and the Browser changes are Live workflows rather than Suite-only devices.
- **Expressive Chords** is included with Live 12 Intro, Standard, and Suite, and requires version 12.2 or later.
- **Roar** and **Meld** are Live 12 Suite devices. Other effects demonstrated in the video also depend on the installed edition.

Use Ableton’s [Live edition comparison](https://www.ableton.com/en/live/compare-editions/) before expecting a device from the video to appear in the Browser.

## Bounce a variation to a new audio track

Bounce to New Track renders a selected clip or time selection to audio while preserving the original material. It is useful for producing a transition, reversing a processed phrase, or making a variation that can be edited independently.

1. In Arrangement View, select one or more clips on a single track, or make a time selection across a track.
2. Right-click the selection and choose **Bounce to New Track**. You can also press `Ctrl`-`B` on Windows or `Cmd`-`B` on macOS.
3. Live creates an audio track below the source track with the rendered audio, then mutes the source clips or selection to prevent doubled playback.
4. Edit the new audio clip without altering the original MIDI notes, audio clip, or device chain.

The bounce includes the source track’s device processing but not its mixer adjustments, such as volume, panning, and sends; those mixer settings are copied to the new track. **Bounce Track in Place** is different: it renders the entire source track and replaces it. The current [Bounce to Audio manual section](https://www.ableton.com/en/live-manual/12/bounce-to-audio/) explains the behavior in Arrangement and Session Views.

## Build chords from single MIDI notes

Expressive Chords is a Max for Live device that turns individual MIDI notes into voiced chords. If it is not installed, download it from its Pack page or from the Packs label in Live’s Browser, then add it to a MIDI track before the instrument you want to play.

Start with one of the supplied chord sets and record or enter a simple single-note MIDI pattern. Play the track, then adjust the device’s chord and expression settings while listening in the context of the Set. Use the device’s preset or Hot-Swap control to audition another chord set without replacing the MIDI pattern.

The device supports chord articulation, inversion, dynamics, and MPE expression. It can also use custom chord sets made from MIDI clips, so it is a practical way to turn an existing harmonic idea into a playable part. Ableton’s [Expressive Chords page](https://www.ableton.com/en/packs/expressive-chords/) lists the current Pack requirements and capabilities.

## Shape audio with the redesigned Auto Filter

Live 12.2 introduced a revised Auto Filter interface with a real-time display, updated modulation and mixing controls, and additional filter types. Add **Auto Filter** from the Audio Effects label to an audio or MIDI track, then begin with a simple, audible source such as a loop, sustained pad, or drum bus.

Choose a filter type and adjust the main frequency control while the track plays. The current Auto Filter includes low-pass, high-pass, band-pass, notch, Morph, DJ, Comb, Resampling, Notch + LP, and Vowel options. The display shows the selected filter curve, its modulation, and the output spectrum.

For a controlled first experiment, use a low-pass filter to reduce brightness, then add a small amount of LFO or envelope movement. To explore the new creative modes, try Comb for resonant, flanger-like motion, Vowel for formant-like shaping, or Resampling for deliberate aliasing and degradation. The [Auto Filter reference](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#auto-filter) documents the current filter types and parameters.

## Explore the 12.2 updates to sound-design devices

The video also shows improvements to several devices. Check the edition before loading them, and begin with a preset so that a single new control can be heard clearly.

- **Roar** gained a **Delay** routing mode and a **Dispersion** filter type. Its new MIDI sidechain can control feedback pitch in Note mode, and its envelope follower can use external audio.
- **Meld** gained a four-voice **Chord** oscillator. Its macro controls adjust or modulate chord shape and inversion, and the device also added a Scrambler LFO effect.
- **Resonators** and **Spectral Resonator** gained support for Live’s scale awareness and tuning systems. Spectral Resonator can quantize its harmonics to the active scale, tuning system, or chromatic pitches.

These additions are not replacements for the original devices or their basic workflow. Load one of the new modes, compare it with the original setting, and use the device activator to judge the change at a matched output level. Ableton’s [Live 12.2 announcement](https://www.ableton.com/en/blog/live-12-2-is-out-now/) and current [audio-effect reference](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/) provide the latest device details.

## Organize and tag Browser content more directly

Live 12.2 refined the tag-based Browser introduced in Live 12. Select an item in the Browser and use the **Quick Tags** panel above the Preview tab to view the item’s assigned tags, add user tags, or remove user-created and automatically assigned tags. Factory tags cannot be edited or removed.

Use the Filter View menu next to the Show/Hide Filter View control to show or hide the Quick Tags panel, filter groups, and Tag Editor. In the content pane, open the Content Options menu to choose which metadata columns appear, drag column headers to reorder them, and click a column header to sort the list. You can also assign an available custom icon by right-clicking an eligible Library label or user folder.

These changes are intended to make personal content easier to find without moving it into a different folder structure. Ableton’s [Live 12 Browser guide](https://help.ableton.com/hc/en-us/articles/12927340213660-The-Live-12-Browser) explains the current tag, column, and icon options.

## Keep later Live 12 changes separate

Live 12.2 is a defined point-release milestone. The source video does not cover features added in subsequent Live 12 versions, such as group-track bouncing, Paste Bounced Audio, or later device and Browser changes. Use the current release notes when a command or control does not match the video exactly.

For further reference, see Ableton’s [Live 12.2 announcement](https://www.ableton.com/en/blog/live-12-2-is-out-now/), the [Live 12 reference manual](https://www.ableton.com/en/live-manual/12/), and the canonical source video, [What's new in Ableton Live 12.2? | Feature Overview](https://www.youtube.com/watch?v=E4e5-LhpkGg).
