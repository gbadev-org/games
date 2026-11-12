# Lander Advance

![Title Screen](pictures/title.png)

A first person Lunar Lander-like game for the Game Boy Advance — made for the [GBA Jam 2026](https://itch.io/jam/gbajam26).

## Requirements

- [devkitARM](https://devkitpro.org/wiki/Getting_Started) (devkitPro)
- [grit](https://www.coranac.com/projects/grit/) (included with devkitPro)

## Build

```bash
make
```

The resulting `lander-advance.gba` can be run on mGBA, NanoBoyAdvance or real hardware via flashcart.

```bash
make clean   # remove build artifacts
```

## How to play

**Flight & Manoeuvring Controls (Cockpit) - How to avoid crashing into bits.**
- A: Main Engine - Fires the primary vertical thruster to counteract gravity. Consumes propellant.
- D-PAD Left / Right: Lateral RCS - Delivers horizontal manoeuvring thrust to the left or right.
- D-PAD Up / Down: Vertical RCS - Delivers translational thrust upwards or downwards.
- L / R (Shoulders): LEM Rotation - Clockwise (L) or counter-clockwise (R) roll attitude.
- SELECT: Popipopi. Press it. Go on, do it.
- START: Flight pause: pause is pause.

**Auxiliary Systems: Radar and Spotlight**
- B + R: Onboard Radar - Toggles radar scanning for the touchdown pad.
  CAUTION: The radar engages as soon as you activate it, both inside and outside the landing zone, but only if you are below 200 metres of altitude.
- B + L: Landing Lights (Spotlight) - Toggles the high-intensity searchlight illuminating the ground below.
- Warning Light: When you are outside the landing zone and below the descent procedure starting altitude (200 m), the warning light will illuminate on your screen. Don't get distracted, it's very large.

**Regarding energy consumption:**
The landing light functions ONLY and EXCLUSIVELY in Night Mode!
If you are in Day Mode and attempt to turn it on, the light will NOT illuminate (seeing as the sun is already out, don't be greedy), BUT YOU WILL STILL CONSUME 1 UNIT OF BATTERY POWER!
Avoid pressing buttons at random; you're supposed to be a professional.

**Menu Navigation Controls**
In selection, configuration, and pause menus:
- A: Confirm / Advance - Selects highlighted option, opens technical dossiers, launches flight, or confirms Game Mode (Simulation/Fast), landing area, or lander.
- B: Back / Cancel - Returns to the previous screen or cancels the last selection.
- D-PAD Up / Down: Cursor Movement - Selects Game Mode (Simulation / Fast), navigates vertically through landing areas and pause menu entries.
- D-PAD Left / Right: Value Adjustment - Toggles Flight Mode (Day Mode / Night Mode), cycles through celestial bodies and landers, adjusts crew headcount.
- START: Pause - Opens the pause menu during flight.

Check the manual for full information.

## Team

- **Ernesto De Felice**
- **Pierluca De Felice**
- **Raffaele Colamarino**
- **Raffaele Aucelli**

## License

- **Code:** MIT — see [LICENSE](LICENSE)
- **Assets** (graphics, audio): CC BY 4.0 — see [ASSETS_LICENSE](ASSETS_LICENSE)

See [CREDITS.md](CREDITS.md) for full credits and third-party attributions.
