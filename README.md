ATTYR – Intelligent Fashion Recommendation System

ATTYR is an end-to-end AI-powered fashion assistant that:

- Removes background from clothing images
- Classifies garment types using deep learning
- Builds a virtual wardrobe
- Extracts metadata
- Generates outfit recommendations
- Visually displays outfit suggestions side-by-side


**🧠 System Architecture**

Pipeline:

1. Background Removal(U²-Net via rembg)
2. Garment Classification (MobileNetV2 – baseline)
3. Metadata Extraction
4. Virtual Wardrobe Construction
5. Outfit Recommendation Engine
6. Visual Recommendation Display


**📁 Project Structure**


attyr_core/
│
├── segmentation/
├── classification/
├── metadata/
├── recommendation/
│
├── requirements.txt
├── README.md
└── .gitignore


**⚙️ Setup Instructions**

1️⃣ Create virtual environment

python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies

        pip install -r requirements.txt

    🚀 Usage

    Segment Dataset
        python segmentation/segment_dataset.py
    Train Garment Classifier
        python classification/train.py
    Build Virtual Wardrobe
        python metadata/build_wardrobe.py
    Generate Outfit Recommendations
        python recommendation/recommend.py

**📌 Notes**

Model weights (*.pth) are excluded from the repository.

Datasets are excluded to keep repository lightweight.

This repository represents the baseline implementation.

Future upgrades include embedding-based compatibility modeling and improved metadata extraction.

**🎯 Project Status**

Baseline system completed and functional.

Next phase:

Embedding-based recommendation

Improved garment understanding

Learned compatibility modeling
