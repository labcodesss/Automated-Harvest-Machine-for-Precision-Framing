import os
from scripts.capture_image import capture_image
from scripts.predict import predict_class

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(project_root, 'images')
    os.makedirs(images_dir, exist_ok=True)
    img_path = os.path.join(images_dir, 'captured.jpg')

    print("=== Areca Nut Classifier ===")
    print("1 - Capture and classify new image")
    print("2 - Test with existing image")
    choice = input("Choose mode (1 or 2): ").strip()

    if choice == '1':
        # Capture new image mode
        success = capture_image(save_path=img_path)
        if not success:
            print("Image capture failed")
            return

        result = predict_class(img_path, debug=True)
        print("\n=== Classification Result ===")
        print(f"Prediction: {result['final_prediction']}")
        print(f"Confidence: {result['model_confidence']:.1f}%")
        print(f"Details: {result['message']}")

    elif choice == '2':
        # Test existing image mode
        test_dir = os.path.join(project_root, 'test_samples')
        os.makedirs(test_dir, exist_ok=True)
        
        print("\nInstructions:")
        print(f"1. Place any test image (ripe/unripe/rotten/not_valid) in:")
        print(f"   {test_dir}")
        print("2. Make sure only one image is present")
        input("Press Enter when ready...")
        
        # Find first available image
        test_files = []
        for ext in ('*.jpg', '*.jpeg', '*.png'):
            test_files.extend([f for f in os.listdir(test_dir) if f.lower().endswith(ext[1:])])
        
        if not test_files:
            print("\nError: No test images found!")
            print(f"Please place an image in {test_dir}")
            return
            
        test_path = os.path.join(test_dir, test_files[0])
        print(f"\nTesting image: {test_files[0]}")
        
        result = predict_class(test_path, debug=True)
        print("\n=== Test Result ===")
        print(f"Prediction: {result['final_prediction']}")
        print(f"Confidence: {result['model_confidence']:.1f}%")
        print(f"Details: {result['message']}")
        
        # Clean up
        if len(test_files) > 1:
            print("\nWarning: Multiple images found in test_samples")
            print("Using first image only")

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()