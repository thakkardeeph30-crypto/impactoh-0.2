import subprocess
import os

assets_config = [
    {
        "filename": "impactoh-logo",
        "width": 800,
        "height": 260,
        "bg": "#2B231B",
        "title": "ImpactOh",
        "subtitle": "SMART IMPACT DETECTION • LUGGAGE ACCESSORY",
        "tag": "OFFICIAL BRAND IDENTITY",
        "body": '''
        <g transform="translate(140, 75)">
            <!-- Brand Icon -->
            <rect x="0" y="0" width="84" height="84" rx="22" fill="#EF7625" />
            <!-- Concentric shock ring geometry -->
            <circle cx="42" cy="42" r="26" fill="none" stroke="#2B231B" stroke-width="5" stroke-dasharray="12 4"/>
            <circle cx="42" cy="42" r="16" fill="#FFF8F2" />
            <circle cx="42" cy="42" r="7" fill="#2B231B" />
            <path d="M 22 18 C 30 10, 54 10, 62 18" fill="none" stroke="#FFF8F2" stroke-width="4" stroke-linecap="round"/>
            <!-- Brand Wordmark -->
            <text x="108" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif" font-size="52" font-weight="900" fill="#FFF8F2" letter-spacing="-1.5">Impact<tspan fill="#EF7625">Oh</tspan></text>
            <!-- Badge -->
            <rect x="360" y="28" width="145" height="28" rx="8" fill="#EF7625" fill-opacity="0.18" stroke="#EF7625" stroke-width="1.4"/>
            <text x="432" y="47" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace" font-size="11" font-weight="800" fill="#EF7625" text-anchor="middle" letter-spacing="1.5">STARTUP STUDY</text>
        </g>
        '''
    },
    {
        "filename": "product",
        "width": 1200,
        "height": 800,
        "bg": "#231B14",
        "title": "ImpactOh Product Concept Architecture",
        "subtitle": "Modular luggage accessory combining everyday personalization with internal impact detection",
        "tag": "STAGE 04: PRODUCT CONCEPT",
        "body": '''
        <g transform="translate(600, 360)">
            <!-- Exploded schematic view of the accessory -->
            <!-- 1. Luggage Strap Connector -->
            <g transform="translate(-360, -40)">
                <rect x="-30" y="-20" width="60" height="120" rx="14" fill="#2B231B" stroke="#EF7625" stroke-width="2"/>
                <path d="M -15 20 C -15 0, 15 0, 15 20 L 15 60 C 15 80, -15 80, -15 60 Z" fill="#FFF8F2" fill-opacity="0.1"/>
                <text x="0" y="125" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">STRAP MOUNT</text>
            </g>
            <line x1="-330" y1="20" x2="-240" y2="20" stroke="#EF7625" stroke-width="2" stroke-dasharray="6 4"/>

            <!-- 2. Main Enclosure (Chassis) -->
            <g transform="translate(-100, -80)">
                <rect x="-120" y="-40" width="240" height="200" rx="24" fill="#2B231B" stroke="#EF7625" stroke-width="2.5"/>
                <rect x="-100" y="-20" width="200" height="160" rx="16" fill="#1C1611" stroke="#FFF8F2" stroke-opacity="0.15" stroke-width="1.5"/>
                <!-- Internal mechanism pocket -->
                <rect x="-70" y="10" width="140" height="100" rx="12" fill="#261E17" stroke="#EF7625" stroke-width="1.5" stroke-dasharray="6 4"/>
                <text x="0" y="45" font-family="sans-serif" font-size="12" font-weight="700" fill="#EF7625" text-anchor="middle">INTERNAL CAVITY</text>
                <text x="0" y="65" font-family="sans-serif" font-size="11" fill="#FFF8F2" opacity="0.8" text-anchor="middle">Houses Spring &amp; Latch</text>
                <text x="0" y="85" font-family="monospace" font-size="10" fill="#FFF8F2" opacity="0.5" text-anchor="middle">Depth: 14mm • Travel: 8mm</text>
                <text x="0" y="185" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">01. BASE CHASSIS</text>
            </g>
            <line x1="20" y1="20" x2="110" y2="20" stroke="#EF7625" stroke-width="2" stroke-dasharray="6 4"/>

            <!-- 3. Customizable Faceplate &amp; Sensor Lens -->
            <g transform="translate(240, -80)">
                <rect x="-100" y="-40" width="200" height="200" rx="24" fill="#EF7625" fill-opacity="0.1" stroke="#EF7625" stroke-width="2.5"/>
                <rect x="-80" y="-20" width="160" height="160" rx="18" fill="#FFF0E5" fill-opacity="0.06" stroke="#FFF8F2" stroke-width="2"/>
                <!-- Badge custom graphics placeholder -->
                <circle cx="0" cy="35" r="38" fill="#EF7625" />
                <path d="M -15 35 L 0 50 L 22 24" fill="none" stroke="#2B231B" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
                <!-- Indicator Window Aperture -->
                <rect x="-50" y="85" width="100" height="26" rx="8" fill="#2B231B" stroke="#FFF8F2" stroke-width="1.5"/>
                <text x="0" y="102" font-family="monospace" font-size="10" font-weight="700" fill="#EF7625" text-anchor="middle">STATUS WINDOW</text>
                <text x="0" y="185" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">02. MODULAR FACEPLATE</text>
            </g>

            <!-- Bottom Specs Bar -->
            <rect x="-420" y="170" width="840" height="42" rx="10" fill="#1A140F" stroke="#FFF8F2" stroke-opacity="0.1"/>
            <text x="-400" y="196" font-family="monospace" font-size="12" fill="#FFF8F2" opacity="0.8">DIMENSIONS: 68 × 48 × 16 mm</text>
            <text x="0" y="196" font-family="monospace" font-size="12" fill="#EF7625" text-anchor="middle">WEIGHT ESTIMATE: &lt; 38g</text>
            <text x="400" y="196" font-family="monospace" font-size="12" fill="#FFF8F2" opacity="0.8" text-anchor="end">INTERFACE: QUICK-RELEASE CLAMP</text>
        </g>
        '''
    },
    {
        "filename": "competitor-research",
        "width": 1200,
        "height": 800,
        "bg": "#211B15",
        "title": "Existing Solutions &amp; Competitor Research Matrix",
        "subtitle": "Analysis of industrial transit sensors (e.g. ShockWatch) vs. the consumer-oriented ImpactOh design",
        "tag": "STAGE 02: COMPETITOR BENCHMARK",
        "body": '''
        <g transform="translate(600, 350)">
            <!-- Left Side: Existing Industrial Indicators -->
            <g transform="translate(-290, 0)">
                <rect x="-240" y="-170" width="480" height="340" rx="16" fill="#1B1510" stroke="#FFF8F2" stroke-opacity="0.2" stroke-width="2"/>
                <rect x="-240" y="-170" width="480" height="46" rx="16 16 0 0" fill="#2B231B"/>
                <text x="-215" y="-140" font-family="sans-serif" font-size="16" font-weight="800" fill="#FFF8F2">Existing Impact Indicators (e.g. ShockWatch)</text>
                
                <!-- Schematic of industrial shock tube -->
                <g transform="translate(0, -70)">
                    <rect x="-160" y="-22" width="320" height="44" rx="10" fill="#261E17" stroke="#FFF8F2" stroke-opacity="0.3"/>
                    <rect x="-100" y="-8" width="200" height="16" rx="6" fill="#140E0A" stroke="#FFF8F2" stroke-opacity="0.5"/>
                    <circle cx="-60" cy="0" r="6" fill="#FF5252"/>
                    <text x="0" y="28" font-family="monospace" font-size="10" fill="#FFF8F2" opacity="0.6" text-anchor="middle">CAPILLARY DYE / TUBE SENSOR</text>
                </g>

                <!-- Points -->
                <g transform="translate(-215, 0)" font-family="sans-serif" font-size="13" fill="#FFF8F2">
                    <text y="0" opacity="0.9"><tspan fill="#FF7043" font-weight="700">Primary Purpose:</tspan> Freight damage claims &amp; freight insurance</text>
                    <text y="30" opacity="0.9"><tspan fill="#FF7043" font-weight="700">Target Usage:</tspan> Industrial logistics, heavy pallet shipping</text>
                    <text y="60" opacity="0.9"><tspan fill="#FF7043" font-weight="700">Product Form:</tspan> Adhesive warning label sticker</text>
                    <text y="90" opacity="0.9"><tspan fill="#FF7043" font-weight="700">Personalization:</tspan> None — purely warning-oriented</text>
                    <text y="120" opacity="0.9"><tspan fill="#FF7043" font-weight="700">Consumer Fit:</tspan> Low consumer adoption and everyday appeal</text>
                </g>
            </g>

            <!-- Center VS Icon -->
            <circle cx="0" cy="0" r="28" fill="#EF7625" />
            <text x="0" y="6" font-family="sans-serif" font-size="16" font-weight="900" fill="#2B231B" text-anchor="middle">VS</text>

            <!-- Right Side: ImpactOh Approach -->
            <g transform="translate(290, 0)">
                <rect x="-240" y="-170" width="480" height="340" rx="16" fill="#291F17" stroke="#EF7625" stroke-width="2.5"/>
                <rect x="-240" y="-170" width="480" height="46" rx="16 16 0 0" fill="#EF7625"/>
                <text x="-215" y="-140" font-family="sans-serif" font-size="16" font-weight="800" fill="#2B231B">ImpactOh Design Direction</text>
                
                <!-- Schematic of consumer modular badge -->
                <g transform="translate(0, -70)">
                    <rect x="-140" y="-22" width="280" height="44" rx="12" fill="#1C1611" stroke="#EF7625" stroke-width="1.8"/>
                    <rect x="-120" y="-14" width="70" height="28" rx="8" fill="#EF7625" />
                    <text x="-85" y="4" font-family="sans-serif" font-size="10" font-weight="800" fill="#2B231B" text-anchor="middle">BADGE</text>
                    <circle cx="20" cy="0" r="10" fill="#FFF8F2" stroke="#EF7625" stroke-width="2"/>
                    <text x="75" y="4" font-family="sans-serif" font-size="10" font-weight="700" fill="#EF7625">CLIP LOCK</text>
                    <text x="0" y="28" font-family="monospace" font-size="10" fill="#EF7625" text-anchor="middle">CONSUMER LUGGAGE ACCESSORY</text>
                </g>

                <!-- Points -->
                <g transform="translate(-215, 0)" font-family="sans-serif" font-size="13" fill="#FFF8F2">
                    <text y="0" opacity="0.95"><tspan fill="#EF7625" font-weight="700">Primary Purpose:</tspan> Luggage personality + Impact awareness</text>
                    <text y="30" opacity="0.95"><tspan fill="#EF7625" font-weight="700">Target Usage:</tspan> Frequent flyers, modern travel &amp; backpacks</text>
                    <text y="60" opacity="0.95"><tspan fill="#EF7625" font-weight="700">Product Form:</tspan> Reusable, durable clip-on luggage accessory</text>
                    <text y="90" opacity="0.95"><tspan fill="#EF7625" font-weight="700">Personalization:</tspan> High — collectible, customizable faceplates</text>
                    <text y="120" opacity="0.95"><tspan fill="#EF7625" font-weight="700">Consumer Fit:</tspan> High everyday appeal and aesthetic identity</text>
                </g>
            </g>
        </g>
        '''
    },
    {
        "filename": "mechanism",
        "width": 1200,
        "height": 800,
        "bg": "#221A13",
        "title": "Conceptual Mechanical Shock Mechanism",
        "subtitle": "Kinematic movement response, calibrated spring threshold, and mechanical locking flag",
        "tag": "STAGE 05: MECHANISM DEVELOPMENT",
        "body": '''
        <g transform="translate(600, 350)">
            <!-- Main Mechanism Assembly Diagram -->
            <rect x="-480" y="-150" width="960" height="300" rx="20" fill="#19130D" stroke="#EF7625" stroke-width="2"/>
            
            <!-- Anchor Block -->
            <g transform="translate(-400, 0)">
                <rect x="-40" y="-90" width="80" height="180" rx="10" fill="#2B231B" stroke="#FFF8F2" stroke-opacity="0.3" stroke-width="2"/>
                <line x1="-30" y1="-70" x2="30" y2="-70" stroke="#EF7625" stroke-width="2"/>
                <line x1="-30" y1="0" x2="30" y2="0" stroke="#EF7625" stroke-width="2"/>
                <line x1="-30" y1="70" x2="30" y2="70" stroke="#EF7625" stroke-width="2"/>
                <text x="0" y="115" font-family="monospace" font-size="11" fill="#FFF8F2" opacity="0.7" text-anchor="middle">CHASSIS ANCHOR</text>
            </g>

            <!-- Pre-loaded Compression Spring -->
            <g transform="translate(-250, 0)">
                <path d="M -90 0 L -70 -40 L -40 40 L -10 -40 L 20 40 L 50 -40 L 70 40 L 90 0" fill="none" stroke="#EF7625" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                <text x="0" y="68" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">PRE-LOADED SPRING</text>
                <text x="0" y="85" font-family="sans-serif" font-size="10" fill="#FFF8F2" opacity="0.6" text-anchor="middle">Calibrated Force Threshold</text>
            </g>

            <!-- Inertial Travel Mass -->
            <g transform="translate(-60, 0)">
                <rect x="-70" y="-70" width="140" height="140" rx="14" fill="#EF7625" stroke="#FFF8F2" stroke-width="2.5"/>
                <text x="0" y="-12" font-family="sans-serif" font-size="15" font-weight="900" fill="#2B231B" text-anchor="middle">INERTIAL</text>
                <text x="0" y="8" font-family="sans-serif" font-size="15" font-weight="900" fill="#2B231B" text-anchor="middle">MASS</text>
                <text x="0" y="30" font-family="monospace" font-size="10" fill="#2B231B" text-anchor="middle">m = 8.5g</text>
                
                <!-- Travel Vector -->
                <path d="M -50 -90 L 50 -90" stroke="#FFF8F2" stroke-width="2" marker-end="url(#arrow)"/>
                <text x="0" y="-100" font-family="monospace" font-size="11" fill="#FFF8F2" text-anchor="middle">TRAVEL PATH →</text>
                <text x="0" y="115" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">SLIDING CORE</text>
            </g>

            <!-- Detent &amp; Mechanical Latch -->
            <g transform="translate(130, 0)">
                <path d="M -30 -30 L 10 -30 L 40 0 L 10 30 L -30 30 Z" fill="#2B231B" stroke="#FFF8F2" stroke-width="2.5"/>
                <circle cx="10" cy="0" r="8" fill="#EF7625"/>
                <text x="0" y="68" font-family="monospace" font-size="11" fill="#FFF8F2" opacity="0.9" text-anchor="middle">RETENTION LATCH</text>
                <text x="0" y="85" font-family="sans-serif" font-size="10" fill="#FFF8F2" opacity="0.6" text-anchor="middle">Prevents False Trigger</text>
                <text x="0" y="115" font-family="monospace" font-size="11" fill="#FFF8F2" opacity="0.7" text-anchor="middle">DETENT GATE</text>
            </g>

            <!-- Trigger Status Window -->
            <g transform="translate(340, 0)">
                <rect x="-80" y="-70" width="160" height="140" rx="16" fill="#120D08" stroke="#EF7625" stroke-width="3"/>
                <!-- Color Indicator Flag -->
                <rect x="-60" y="-45" width="120" height="90" rx="10" fill="#EF7625" />
                <text x="0" y="-5" font-family="sans-serif" font-size="14" font-weight="900" fill="#2B231B" text-anchor="middle">IMPACT</text>
                <text x="0" y="18" font-family="sans-serif" font-size="13" font-weight="900" fill="#2B231B" text-anchor="middle">EXPOSED</text>
                <text x="0" y="115" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="middle">LOCKED DISPLAY</text>
            </g>

            <!-- Technical Disclaimer Notice -->
            <rect x="-480" y="180" width="960" height="38" rx="8" fill="#2B231B" stroke="#EF7625" stroke-width="1"/>
            <text x="0" y="204" font-family="sans-serif" font-size="11" fill="#FFF8F2" text-anchor="middle">
                <tspan fill="#EF7625" font-weight="700">ENGINEERING STATUS: </tspan>Digital kinematic model complete. Physical calibration &amp; threshold testing pending physical fabrication.
            </text>
        </g>
        '''
    },
    {
        "filename": "cad",
        "width": 1200,
        "height": 800,
        "bg": "#1D1711",
        "title": "3D Solid Modeling &amp; CAD Assembly",
        "subtitle": "Component nesting, wall thickness verification, travel guides and modular accessory chassis",
        "tag": "STAGE 06: CAD DESIGN",
        "body": '''
        <g transform="translate(600, 360)">
            <!-- Isometric CAD Wireframe Schematic -->
            <g transform="translate(-180, -30)">
                <!-- Main body isometric cube -->
                <polygon points="-160,-50 0,-130 160,-50 0,30" fill="#2E2319" stroke="#EF7625" stroke-width="2.5"/>
                <polygon points="-160,-50 0,30 0,140 -160,60" fill="#231A12" stroke="#EF7625" stroke-width="2"/>
                <polygon points="0,30 160,-50 160,60 0,140" fill="#18110A" stroke="#EF7625" stroke-width="2"/>
                
                <!-- Internal core isometric pocket -->
                <polygon points="-90,-25 0,-70 90,-25 0,20" fill="none" stroke="#FFF8F2" stroke-width="1.8" stroke-dasharray="6 4"/>
                <line x1="0" y1="20" x2="0" y2="90" stroke="#FFF8F2" stroke-width="1.8" stroke-dasharray="6 4"/>
                <polygon points="-90,45 0,90 90,45 0,20" fill="none" stroke="#FFF8F2" stroke-width="1.8" stroke-dasharray="6 4"/>
                
                <!-- Dimension Calipers -->
                <line x1="-190" y1="-50" x2="-190" y2="60" stroke="#EF7625" stroke-width="1.5"/>
                <line x1="-180" y1="-50" x2="-200" y2="-50" stroke="#EF7625" stroke-width="1.5"/>
                <line x1="-180" y1="60" x2="-200" y2="60" stroke="#EF7625" stroke-width="1.5"/>
                <text x="-215" y="10" font-family="monospace" font-size="12" fill="#EF7625" text-anchor="end">48.0 mm</text>

                <line x1="20" y1="165" x2="175" y2="85" stroke="#EF7625" stroke-width="1.5"/>
                <text x="120" y="150" font-family="monospace" font-size="12" fill="#EF7625">68.0 mm</text>
            </g>

            <!-- CAD Assembly Sidebar Specs -->
            <g transform="translate(180, -140)">
                <rect x="0" y="0" width="340" height="280" rx="14" fill="#241B13" stroke="#FFF8F2" stroke-opacity="0.2" stroke-width="1.5"/>
                <rect x="0" y="0" width="340" height="38" rx="14 14 0 0" fill="#2B231B"/>
                <text x="20" y="24" font-family="sans-serif" font-size="12" font-weight="800" fill="#EF7625" letter-spacing="1">CAD ASSEMBLY SPECIFICATION</text>
                
                <g transform="translate(20, 65)" font-family="monospace" font-size="12" fill="#FFF8F2">
                    <text y="0"><tspan fill="#EF7625">▪ Part 01:</tspan> Upper Top Shell (1.8mm Wall)</text>
                    <text y="30"><tspan fill="#EF7625">▪ Part 02:</tspan> Sliding Inertial Sled (ABS)</text>
                    <text y="60"><tspan fill="#EF7625">▪ Part 03:</tspan> Linear Spring Guide Track</text>
                    <text y="90"><tspan fill="#EF7625">▪ Part 04:</tspan> Base Mounting Carrier</text>
                    <text y="120"><tspan fill="#EF7625">▪ Part 05:</tspan> Quick-Snap Luggage Clip</text>
                    <line x1="0" y1="145" x2="300" y2="145" stroke="#FFF8F2" stroke-opacity="0.1" stroke-width="1"/>
                    <text y="170" fill="#27C93F">✓ Tolerance Audit: PASS (±0.25mm)</text>
                    <text y="195" fill="#EF7625">✓ Export Format: STEP / STL (Fusion 360)</text>
                </g>
            </g>
        </g>
        '''
    },
    {
        "filename": "fusion360",
        "width": 1200,
        "height": 800,
        "bg": "#1C1610",
        "title": "Autodesk Fusion 360 Design Review",
        "subtitle": "Digital design verification, clearance checking, kinematic motion analysis and pre-print review",
        "tag": "STAGE 07: FUSION 360 AUDIT",
        "body": '''
        <g transform="translate(600, 350)">
            <!-- Software Window Shell -->
            <rect x="-480" y="-170" width="960" height="340" rx="14" fill="#140F0A" stroke="#FFF8F2" stroke-opacity="0.25" stroke-width="2"/>
            
            <!-- Window Header -->
            <rect x="-480" y="-170" width="960" height="36" rx="14 14 0 0" fill="#2B231B"/>
            <circle cx="-455" cy="-152" r="5" fill="#FF5F56"/>
            <circle cx="-440" cy="-152" r="5" fill="#FFBD2E"/>
            <circle cx="-425" cy="-152" r="5" fill="#27C93F"/>
            <text x="-400" y="-147" font-family="sans-serif" font-size="12" fill="#FFF8F2" opacity="0.8">Autodesk Fusion 360 — ImpactOh_Proto_v5_Final.f3d</text>
            <text x="450" y="-147" font-family="monospace" font-size="11" fill="#EF7625" text-anchor="end">DESIGN WORKSPACE: MODEL</text>

            <!-- 3D Canvas Area -->
            <g transform="translate(-150, 20)">
                <rect x="-300" y="-140" width="600" height="260" rx="10" fill="#18120B" stroke="#EF7625" stroke-opacity="0.25" stroke-width="1.5"/>
                <!-- Coordinate Axes -->
                <line x1="-270" y1="90" x2="-230" y2="90" stroke="#FF5252" stroke-width="2"/>
                <text x="-225" y="94" font-family="monospace" font-size="10" fill="#FF5252">X</text>
                <line x1="-270" y1="90" x2="-270" y2="50" stroke="#27C93F" stroke-width="2"/>
                <text x="-270" y="44" font-family="monospace" font-size="10" fill="#27C93F">Y</text>
                <line x1="-270" y1="90" x2="-295" y2="105" stroke="#448AFF" stroke-width="2"/>
                <text x="-300" y="115" font-family="monospace" font-size="10" fill="#448AFF">Z</text>

                <!-- 3D Model Wireframe Representation -->
                <ellipse cx="0" cy="20" rx="180" ry="70" fill="none" stroke="#EF7625" stroke-width="2"/>
                <ellipse cx="0" cy="-20" rx="140" ry="50" fill="none" stroke="#FFF8F2" stroke-width="1.8" stroke-opacity="0.6"/>
                <line x1="-180" y1="20" x2="-140" y2="-20" stroke="#EF7625" stroke-width="1.5"/>
                <line x1="180" y1="20" x2="140" y2="-20" stroke="#EF7625" stroke-width="1.5"/>
                <circle cx="0" cy="0" r="28" fill="#EF7625" fill-opacity="0.85"/>
                <text x="0" y="5" font-family="sans-serif" font-size="11" font-weight="900" fill="#2B231B" text-anchor="middle">CORE</text>
            </g>

            <!-- Audit Inspection Panel -->
            <g transform="translate(300, 20)">
                <rect x="-130" y="-140" width="260" height="260" rx="10" fill="#241B13" stroke="#FFF8F2" stroke-opacity="0.15" stroke-width="1.5"/>
                <text x="-110" y="-115" font-family="sans-serif" font-size="12" font-weight="800" fill="#EF7625">DESIGN REVIEW AUDIT</text>
                
                <g transform="translate(-110, -80)" font-family="monospace" font-size="11" fill="#FFF8F2">
                    <text y="0">✓ Component Fit</text>
                    <text y="18" fill="#27C93F" font-size="9.5">  No physical collisions</text>
                    
                    <text y="45">✓ Clearance Review</text>
                    <text y="63" fill="#27C93F" font-size="9.5">  0.4mm sliding clearance</text>
                    
                    <text y="90">✓ Motion Path Check</text>
                    <text y="108" fill="#27C93F" font-size="9.5">  Unrestricted linear travel</text>

                    <text y="135">✓ Mesh Integrity</text>
                    <text y="153" fill="#EF7625" font-size="9.5">  Water-tight STL manifold</text>
                </g>
            </g>
        </g>
        '''
    },
    {
        "filename": "material",
        "width": 1200,
        "height": 800,
        "bg": "#221A14",
        "title": "Material Evaluation &amp; Selection Matrix",
        "subtitle": "Systematic assessment across mechanical resilience, availability, manufacturability, and cost",
        "tag": "STAGE 08: MATERIAL FINALISATION",
        "body": '''
        <g transform="translate(600, 350)">
            <!-- 4 Structured Evaluation Criterion Cards -->
            <!-- 1. Mechanical Strength -->
            <g transform="translate(-240, -85)">
                <rect x="-210" y="-70" width="420" height="130" rx="14" fill="#291F17" stroke="#EF7625" stroke-width="2"/>
                <circle cx="-165" cy="-20" r="22" fill="#EF7625" fill-opacity="0.2"/>
                <text x="-165" y="-14" font-family="sans-serif" font-size="14" font-weight="900" fill="#EF7625" text-anchor="middle">01</text>
                <text x="-125" y="-28" font-family="sans-serif" font-size="15" font-weight="800" fill="#FFF8F2">Strength &amp; Shock Resistance</text>
                <text x="-125" y="-8" font-family="sans-serif" font-size="12" fill="#FFF8F2" opacity="0.8">Withstands rough airport conveyor impacts and falls.</text>
                <text x="-125" y="12" font-family="monospace" font-size="11" fill="#EF7625">CRITERION: High impact strength &amp; shear durability</text>
            </g>

            <!-- 2. Availability -->
            <g transform="translate(240, -85)">
                <rect x="-210" y="-70" width="420" height="130" rx="14" fill="#291F17" stroke="#EF7625" stroke-width="2"/>
                <circle cx="-165" cy="-20" r="22" fill="#EF7625" fill-opacity="0.2"/>
                <text x="-165" y="-14" font-family="sans-serif" font-size="14" font-weight="900" fill="#EF7625" text-anchor="middle">02</text>
                <text x="-125" y="-28" font-family="sans-serif" font-size="15" font-weight="800" fill="#FFF8F2">Material Availability</text>
                <text x="-125" y="-8" font-family="sans-serif" font-size="12" fill="#FFF8F2" opacity="0.8">Readily procurable engineering filament and stock.</text>
                <text x="-125" y="12" font-family="monospace" font-size="11" fill="#EF7625">CRITERION: Domestic supply chain reliability</text>
            </g>

            <!-- 3. Manufacturability -->
            <g transform="translate(-240, 75)">
                <rect x="-210" y="-70" width="420" height="130" rx="14" fill="#291F17" stroke="#EF7625" stroke-width="2"/>
                <circle cx="-165" cy="-20" r="22" fill="#EF7625" fill-opacity="0.2"/>
                <text x="-165" y="-14" font-family="sans-serif" font-size="14" font-weight="900" fill="#EF7625" text-anchor="middle">03</text>
                <text x="-125" y="-28" font-family="sans-serif" font-size="15" font-weight="800" fill="#FFF8F2">Manufacturability &amp; Prototyping</text>
                <text x="-125" y="-8" font-family="sans-serif" font-size="12" fill="#FFF8F2" opacity="0.8">Compatible with FDM 3D printing and injection molding.</text>
                <text x="-125" y="12" font-family="monospace" font-size="11" fill="#EF7625">CRITERION: Precise dimensional tolerances (±0.2mm)</text>
            </g>

            <!-- 4. Cost Efficiency -->
            <g transform="translate(240, 75)">
                <rect x="-210" y="-70" width="420" height="130" rx="14" fill="#291F17" stroke="#EF7625" stroke-width="2"/>
                <circle cx="-165" cy="-20" r="22" fill="#EF7625" fill-opacity="0.2"/>
                <text x="-165" y="-14" font-family="sans-serif" font-size="14" font-weight="900" fill="#EF7625" text-anchor="middle">04</text>
                <text x="-125" y="-28" font-family="sans-serif" font-size="15" font-weight="800" fill="#FFF8F2">Cost &amp; Weight Profile</text>
                <text x="-125" y="-8" font-family="sans-serif" font-size="12" fill="#FFF8F2" opacity="0.8">Affordable unit economics without luggage baggage weight penalty.</text>
                <text x="-125" y="12" font-family="monospace" font-size="11" fill="#EF7625">CRITERION: Optimal cost-to-performance ratio</text>
            </g>
        </g>
        '''
    },
    {
        "filename": "prototype",
        "width": 1200,
        "height": 800,
        "bg": "#1E1711",
        "title": "3D-Printed Physical Prototype (Version 1)",
        "subtitle": "Fabricated physical unit from completed CAD design for initial assembly and form-factor verification",
        "tag": "STAGE 09: PHYSICAL PROTOTYPE (VERSION 1 ONLY)",
        "body": '''
        <g transform="translate(600, 350)">
            <!-- Build plate &amp; Additive Manufacturing Graphic -->
            <g transform="translate(-160, 0)">
                <!-- Elliptical heated bed -->
                <ellipse cx="0" cy="90" rx="220" ry="40" fill="#150F0A" stroke="#EF7625" stroke-width="2" stroke-dasharray="8 6"/>
                <ellipse cx="0" cy="90" rx="170" ry="28" fill="#221A12" stroke="#FFF8F2" stroke-opacity="0.3"/>

                <!-- Layered 3D Printed Prototype Model -->
                <path d="M -100 40 C -100 0, 100 0, 100 40 L 100 80 C 100 100, -100 100, -100 80 Z" fill="#EF7625" fill-opacity="0.9" stroke="#FFF8F2" stroke-width="2.5"/>
                <!-- Horizontal FDM layer lines -->
                <line x1="-98" y1="48" x2="98" y2="48" stroke="#2B231B" stroke-width="1.8" stroke-opacity="0.4"/>
                <line x1="-98" y1="56" x2="98" y2="56" stroke="#2B231B" stroke-width="1.8" stroke-opacity="0.4"/>
                <line x1="-98" y1="64" x2="98" y2="64" stroke="#2B231B" stroke-width="1.8" stroke-opacity="0.4"/>
                <line x1="-98" y1="72" x2="98" y2="72" stroke="#2B231B" stroke-width="1.8" stroke-opacity="0.4"/>

                <!-- Faceplate Emblem on 3D Printed Object -->
                <rect x="-50" y="46" width="100" height="26" rx="6" fill="#2B231B"/>
                <text x="0" y="63" font-family="sans-serif" font-size="11" font-weight="900" fill="#FFF8F2" text-anchor="middle">IMPACT<tspan fill="#EF7625">OH</tspan></text>

                <!-- Extruder Nozzle Representation -->
                <polygon points="-12,-60 12,-60 6,-30 -6,-30" fill="#FFF8F2"/>
                <polygon points="-6,-30 6,-30 0,-15" fill="#EF7625"/>
                <line x1="0" y1="-15" x2="0" y2="15" stroke="#EF7625" stroke-width="3" stroke-linecap="round"/>
                <circle cx="0" cy="15" r="4" fill="#FF5252"/>
            </g>

            <!-- Prototype Verification Checklist Card -->
            <g transform="translate(240, -130)">
                <rect x="0" y="0" width="300" height="270" rx="14" fill="#261E16" stroke="#2E7D32" stroke-width="2"/>
                <rect x="0" y="0" width="300" height="38" rx="14 14 0 0" fill="#2E7D32"/>
                <text x="20" y="24" font-family="sans-serif" font-size="12" font-weight="900" fill="#FFFFFF" letter-spacing="1">✓ 3D PRINTING COMPLETED</text>

                <g transform="translate(20, 65)" font-family="monospace" font-size="11.5" fill="#FFF8F2">
                    <text y="0" fill="#27C93F">✓ Physical Unit Fabricated</text>
                    <text y="28" fill="#27C93F">✓ CAD Dimensions Verified</text>
                    <text y="56" fill="#27C93F">✓ Component Fit Evaluated</text>
                    <text y="84" fill="#27C93F">✓ Faceplate Detachable</text>
                    <line x1="0" y1="105" x2="260" y2="105" stroke="#FFF8F2" stroke-opacity="0.1" stroke-width="1"/>
                    <text y="130" fill="#EF7625" font-weight="700">NEXT STAGE (PENDING):</text>
                    <text y="152" fill="#FFF8F2" opacity="0.8">⏳ Impact Drop Testing</text>
                    <text y="174" fill="#FFF8F2" opacity="0.8">⏳ Mechanism Calibration</text>
                </g>
            </g>
        </g>
        '''
    }
]

def generate_svg(item):
    w = item["width"]
    h = item["height"]
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{item['bg']}" />
      <stop offset="100%" stop-color="#140E0A" />
    </linearGradient>
    <pattern id="blueprintGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#FFF8F2" stroke-width="0.75" stroke-opacity="0.04"/>
      <path d="M 200 0 L 0 0 0 200" fill="none" stroke="#EF7625" stroke-width="1" stroke-opacity="0.07"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#EF7625"/>
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect width="100%" height="100%" fill="url(#bgGrad)" />
  <rect width="100%" height="100%" fill="url(#blueprintGrid)" />

  <!-- Outer Technical Border -->
  <rect x="24" y="24" width="{w-48}" height="{h-48}" rx="18" fill="none" stroke="#FFF8F2" stroke-opacity="0.12" stroke-width="1.5" />
  <rect x="34" y="34" width="{w-68}" height="{h-68}" rx="12" fill="none" stroke="#EF7625" stroke-opacity="0.25" stroke-width="1" stroke-dasharray="8 6"/>

  <!-- Corner Brackets -->
  <path d="M 24 55 L 24 24 L 55 24" fill="none" stroke="#EF7625" stroke-width="3"/>
  <path d="M {w-24} 55 L {w-24} 24 L {w-55} 24" fill="none" stroke="#EF7625" stroke-width="3"/>
  <path d="M 24 {h-55} L 24 {h-24} L 55 {h-24}" fill="none" stroke="#EF7625" stroke-width="3"/>
  <path d="M {w-24} {h-55} L {w-24} {h-24} L {w-55} {h-24}" fill="none" stroke="#EF7625" stroke-width="3"/>

  <!-- Top Metadata Header -->
  <g transform="translate(50, 56)">
    <rect x="0" y="0" width="auto" height="24" rx="5" fill="#EF7625" fill-opacity="0.18" stroke="#EF7625" stroke-width="1.2"/>
    <text x="12" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace" font-size="11" font-weight="800" fill="#EF7625" letter-spacing="1.5">{item['tag']}</text>
    <text x="{w - 100}" y="16" font-family="monospace" font-size="11" fill="#FFF8F2" opacity="0.45" text-anchor="end">{w} × {h} PX • PLACEHOLDER</text>
  </g>

  <!-- Body Graphic Schematic -->
  {item['body']}

  <!-- Bottom Title and Annotation (for large placeholders) -->
  {f'''
  <g transform="translate({w / 2}, {h - 85})">
    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif" font-size="23" font-weight="800" fill="#FFF8F2" text-anchor="middle" letter-spacing="-0.4">{item['title']}</text>
    <text x="0" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="400" fill="#FFF8F2" opacity="0.7" text-anchor="middle">{item['subtitle']}</text>
    <text x="0" y="46" font-family="monospace" font-size="10" fill="#EF7625" opacity="0.85" text-anchor="middle">IMPACTOH STARTUP PROJECT • BUZZTECH 50-DAY CHALLENGE</text>
  </g>
  ''' if h > 300 else ''}

</svg>'''

for item in assets_config:
    w = item["width"]
    h = item["height"]
    name = item["filename"]
    svg_path = f"assets/{name}.svg"
    png_path = f"assets/{name}.png"
    
    with open(svg_path, "w") as f:
        f.write(generate_svg(item))
    
    # Render with headless chrome
    abs_svg = os.path.abspath(svg_path)
    subprocess.run([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        f"--screenshot={png_path}",
        f"--window-size={w},{h}",
        "--hide-scrollbars",
        "--default-background-color=00000000",
        f"file://{abs_svg}"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print(f"Generated {png_path} ({w}x{h})")

