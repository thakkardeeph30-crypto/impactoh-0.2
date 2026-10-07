# ImpactOh — Smart Luggage Accessory with Impact Detection

> **BuzzTech 50-Day Startup Challenge**  
> *Personalise Your Luggage. Know When It Takes a Hit.*

[![Pure HTML5](https://img.shields.io/badge/HTML5-Pure%20Semantic-E34F26?logo=html5&logoColor=white)](index.html)
[![Pure CSS3](https://img.shields.io/badge/CSS3-Pure%20Styles-1572B6?logo=css3&logoColor=white)](style.css)
[![Zero JavaScript](https://img.shields.io/badge/JavaScript-None-lightgrey)](#technical-specifications)
[![Responsive](https://img.shields.io/badge/Responsive-Mobile%20%7C%20Tablet%20%7C%20Desktop-green)](#features)

---

## 📌 Overview

**ImpactOh** is a customizable luggage accessory concept engineered to add personality and visual flair to travel baggage while incorporating integrated mechanical impact detection as a functional feature. 

Developed as part of the **BuzzTech 50-Day Startup Challenge**, the project bridges consumer luggage personalisation with physical shock awareness during transit.

---

## 🚀 Key Features

- **Built-in Mechanical Impact Detection**: Uses a passive spring-mass threshold latch mechanism. When baggage experiences shock exceeding calibrated thresholds, the indicator flag triggers without requiring batteries or electronics.
- **Interchangeable Modular Faceplates**: Quick-swap front shells let travelers customize colors, typography, monograms, and iconography.
- **Universal Strap & Handle Mount**: Mounts securely around top handles, telescopic rods, or side luggage straps.
- **Interactive Milestone Switcher (Pure CSS)**: Toggle between **Version 1** (3D printed physical prototype) and **Version 2** (CAD / pre-print phase) dynamically using CSS3 `:has()` pseudo-classes.
- **Full Transparency**: Clearly separates completed CAD/mechanism engineering from pending real-world calibration and drop-testing.

---

## 🛠️ Technical Specifications

This website was built with strict engineering constraints:

- **100% Pure HTML5 & CSS3**: Zero JavaScript (`<script>` tags, event listeners, or inline handlers).
- **No Libraries or Frameworks**: No React, Bootstrap, Tailwind, or external scripts.
- **Responsive Layout**: Designed with fluid CSS Grid, Flexbox, and media queries across mobile, tablet, and ultra-wide screens.
- **Brand Palette**:
  - Primary Orange: `#EF7625`
  - Dark Charcoal: `#2B231B`
  - Off-White Surface: `#FFF8F2`
  - Light Tint: `#FFF0E5`
  - Body Text: `#2D2926`

---

## 📁 Repository Structure

```text
impactoh-0.2/
├── index.html                  # Semantic HTML5 website structure (17 sections)
├── style.css                   # Custom CSS3 stylesheet (Tokens, animations, layout)
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
├── assets/                     # Vector SVGs and high-resolution blueprint diagrams
│   ├── impactoh-logo.png       # Official brand logo (Navbar / Light)
│   ├── impactoh-logo-light.png # High-contrast light brand logo (Footer / Dark)
│   ├── product.png             # Exploded product architecture diagram
│   ├── competitor-research.png # Industrial indicators vs ImpactOh matrix
│   ├── mechanism.png           # Kinematic threshold-latch schematic
│   ├── cad.png                 # Parametric 3D solid model breakdown
│   ├── fusion360.png           # Autodesk Fusion 360 clearance audit
│   ├── material.png            # Engineering material selection matrix
│   └── prototype.png           # Additive manufacturing 3D printed prototype
└── scripts/                    # Asset generator utilities
    ├── generate_assets.py      # Blueprint diagram generation
    └── generate_clean_logo.py  # Logo vector rendering script
```

---

## 🌐 Running Locally

To view the website locally, serve the directory with any static web server:

```bash
# Using Python
python3 -m http.server 8080

# Using Node (npx)
npx serve .
```

Then open `http://localhost:8080/` in any modern web browser.

---

## 🏆 Challenge Acknowledgements

Developed for the **BuzzTech 50-Day Startup Challenge** by the ImpactOh Team.
