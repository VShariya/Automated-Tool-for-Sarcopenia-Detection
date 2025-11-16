# Automated Tool for Sarcopenia Detection

This project presents a deep learning–based pipeline for automatic sarcopenia assessment using abdominal CT scans. The system identifies the L3 vertebra slice, segments key body composition structures, and computes clinically relevant metrics used for sarcopenia screening.

**Key Features**

Automatic L3 Slice Localization using a 3D UNet model (MONAI + PyTorch)

Body Composition Analysis from labeled masks:

Skeletal Muscle Area (SMA)

Subcutaneous Fat Area (SFAT)

Visceral Fat Area (VFAT)

Muscle Density (HU)

Body Area

Sarcopenia Risk Assessment using sex-specific clinical cutoffs

Report Generation

JSON/CSV export of computed metrics

User Interface for easy scan loading, Calculation, and exporting results
**
Tech Stack**

Python, PyTorch, MONAI, Nibabel, Matplotlib

Amazon SageMaker for model training

Amazon S3 for dataset storage and experiment management

Built as part of my final dissertation project

This project presents a deep learning–based pipeline for automatic sarcopenia assessment using abdominal CT scans. The system identifies the L3 vertebra slice, segments key body composition structures, and computes clinically relevant metrics used for sarcopenia screening.

**Key Features**

Automatic L3 Slice Localization using a 3D UNet model (MONAI + PyTorch)

Body Composition Analysis from labeled masks:

Skeletal Muscle Area (SMA)

Subcutaneous Fat Area (SFAT)

Visceral Fat Area (VFAT)

Muscle Density (HU)

Body Area

Sarcopenia Risk Assessment using sex-specific clinical cutoffs

Report Generation

Visual overlay of muscle, SFAT, and VFAT on the L3 slice

JSON/CSV export of computed metrics

User Interface for easy scan loading, visualization, and exporting results

**Tech Stack**

Python, PyTorch, MONAI, Nibabel, Matplotlib

Amazon SageMaker for model training

Amazon S3 for dataset storage and experiment management

Built as part of my final dissertation project

**Goal**

To provide an automated, reproducible, and clinically supportive tool for sarcopenia screening through efficient and accurate body composition analysis.****

To provide an automated, reproducible, and clinically supportive tool for sarcopenia screening through efficient and accurate body composition analysis.
