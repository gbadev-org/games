# Credits

## Team

- **Ernesto De Felice** - Project Lead, Programming, SFX
- **Pierluca De Felice** - Programming, Graphics, SFX
- **Raffaele Colamarino** - Lore, Programming, Game Manual
- **Raffaele Aucelli** - Game Physics, Programming


All the team contributed to the Game Logic, Game Design and Testing.

## Original assets

- **Visual Assets (Cockpit HUD, Lunar Surface, Gauges, UI Digits)**:
  - Created for *Lander Advance* — Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Audio Assets (SFX, Engine Tones)**:
  - Created for *Lander Advance* — Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

# Third-party assets

<!-- List any external assets used (graphics, audio, fonts) with author, license and link -->

- **GBA Jam 2026 Logo** (adapted):
  - **Author:** PyroPyro and kva64
  - **Source:** https://github.com/gbadev-org/gbajam26-assets
  - **License:** CC BY-NC 4.0 — https://creativecommons.org/licenses/by-nc/4.0/
  - **Modifications:** Canvas resized for use in game splash screen

- **"JAM 2026" logo font — H. H. Samuel**:
  - **Author:** deFharo
  - **Source:** https://fontlibrary.org/en/font/h-h-samuel
  - **License:** SIL Open Font License (OFL)

## itch.io Banner (photo composite)
- **Apollo 8 Earthrise**
  - Credit: NASA
  - Source: https://science.nasa.gov/resource/the-rising-earth-as-seen-by-apollo-8/

- **Mars Perseverance Sol 1301 — Right Navigation Camera (Navcam)**
  - Credit: NASA/JPL-Caltech
  - Date: Oct. 17, 2024
  - Source: https://mars.nasa.gov/mars2020/multimedia/raw-images/NRF_1301_0782440641_817ECM_N0610268NCAM13301_01_195J

Used per NASA's Media Usage Guidelines / JPL Image Use Policy. 
No endorsement by NASA, JPL, or Caltech implied.

# Third-Party Code, Libraries & Toolchain

## Tonc & Tonc Text Engine (TTE)
- **Purpose:** Game Boy Advance support library (headers, core utilities, fixed-point math LUTs, affine transformations, default 8x8 font & text engine)
- **Author:** J. Vijn (Cearn)
- **Original Project:** http://www.coranac.com/projects/#tonc
- **Source (reference):** https://github.com/gbadev-org/libtonc
- **Distribution:** devkitPro / gba-dev toolchain (`libtonc`)
- **License:** MIT License

  Copyright (c) 2001-2008 J. Vijn

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.

## libgba
- **Purpose:** Low-level GBA register definitions, interrupts, and BIOS call wrappers
- **Author:** Dave Murphy (WinterMute) / devkitPro
- **Source:** https://github.com/devkitPro/libgba
- **License:** GNU Library General Public License v2 (see `libgba_license.txt`)
- **Attribution:** This project is based in part on the work of the devkitPro 
  project (https://github.com/devkitPro/libgba/blob/master/libgba_license.txt)

## devkitARM & Build Tools
- **devkitARM (GCC for ARM):** GNU Compiler Collection targeting `arm-none-eabi` (GPL)
- **Grit (GBA Raster Image Transmogrifier):** Jasper Vijn (Cearn) — Image to GBA graphics converter (MIT)
- **gbafix:** devkitPro — GBA ROM header patching and checksum tool (GPL)
- **bin2s:** devkitPro — Binary to GNU Assembly conversion utility (GPL)

## newlib
- **Purpose:** C standard library implementation for embedded targets
- **Author:** Red Hat, Inc. / Cygnus Support and various contributors
- **Source:** https://sourceware.org/newlib/
- **Distribution:** devkitARM toolchain
- **License:** Multiple BSD-style licenses (see `COPYING.NEWLIB`)

## libgcc
- **Purpose:** GCC runtime support routines (e.g. software integer/float division)
- **Author:** Free Software Foundation
- **License:** GPL v3 with GCC Runtime Library Exception