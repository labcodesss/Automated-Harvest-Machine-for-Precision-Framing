# Automated-Harvest-Machine-for-Precision-Framing
This project aims to develop an Automated Harvest Machine for precision farming by integrating software and hardware solutions. The software employs image processing and machine learning to identify the ripeness of the crops. Based on this analysis, the hardware system accurately harvests the crop improving efficiency, reducing manual labor.


1. System Overview
Purpose: Automatically classify areca nuts into:
🟠 Ripe (Orange/Yellow)
🟢 Unripe (Green)
⚫ Rotten (Black/Brown)
❌ Not Valid (Other objects)

2. Technical Components
   
A. Core Files
File	               Purpose
main.py	             Main menu & user interface
capture_image.py	   Webcam image capture
preprocess.py	       Image feature extraction
train_model.py	     Machine learning model training
predict.py	         Classification logic
webcam_classify.py	 Real-time classification

B. Key Technologies
OpenCV: Image processing
Scikit-learn: Random Forest classifier
NumPy: Numerical operations
Joblib: Model saving/loading

3. Workflow
   
1. Image Input
   Webcam capture OR test image
   Example: test_samples/unripe.jpg

2.Preprocessing
python
def preprocess_image():
    # Converts to HSV color space
    # Calculates color histograms
    # Extracts dominant color
    # Returns 173-dimensional feature vector
Key Step: Checks if ≥10% of pixels match areca nut colors

3.Classification
  Uses trained Random Forest model
  Fallback to color rules if model unavailable
python
if 5° ≤ hue ≤ 25°: return "ripe"
elif 35° ≤ hue ≤ 85°: return "unripe"
else: return "rotten"

Output

=== Test Result ===
Prediction: unripe 
Confidence: 80.3%
Details: Unripe (80.3%)

5. Key Algorithms
   
A. Color Analysis
HSV Color Space (Better than RGB for color detection)
Hue (H): Color type (0-180° in OpenCV)
Saturation (S): Color purity (0-255)
Value (V): Brightness (0-255)

B. Machine Learning
Random Forest Classifier
100 decision trees
Trained on 173 features per image
Outputs: [ripe_prob, unripe_prob, rotten_prob, not_valid_prob]

6. Confidence Scores
Confidence Range	  Interpretation
≥80%	              Very reliable
60-79%	            Moderately confident
40-59%	            Low confidence (marked "uncertain")
<40%	              Rejected as "not_valid"

7. Sample Output Explained
Processing: test_samples/unripe.jpg 
Coverage: 96.24%        # Excellent nut detection
Dominant HSV: [175 188 135]  # Greenish (H=175°), saturated (S=188)
Prediction: unripe      # Correct classification
Confidence: 80.3%       # High reliability

9. Real-World Applications
   Quality Control in areca nut packaging
   Automated Sorting machines
   Farm Harvest Timing assistance

10. Try It Yourself
Run the system:

python main.py
Test your own images by dropping them in test_samples/

🔧 Technical Details
Feature Extraction
Histogram bins: 50 (Hue), 60 (Saturation), 60 (Value)
Dominant color: Median HSV values
Coverage check: ≥10% areca-colored pixels required

Machine Learning Model
Algorithm: Random Forest Classifier
Parameters: 150 trees, class_weight="balanced"
Features: 173 per image
Accuracy: Typically 85-95% on validation set

📈 Performance Metrics
Class	Accuracy	 Typical   Confidence
Ripe	            90-95%	   85-98%
Unripe	          85-92%	   80-95%
Rotten	          80-88%	   75-92%
Not_Valid	        95-99%	   90-100%

🤝 Contributing
Fork the repository
Create feature branch (git checkout -b feature/improvement)
Commit changes (git commit -am 'Add new feature')
Push to branch (git push origin feature/improvement)
Create Pull Request
   
