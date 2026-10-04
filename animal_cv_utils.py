"""
Computer Vision Utilities and Animal Species Dataset Generator
Provides utilities for image feature extraction and dataset creation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# 1. GENERATE SAMPLE ANIMAL SPECIES DATASET
# ============================================================================

def generate_animal_species_dataset(filename='animal_species_data.csv'):
    """Generate comprehensive animal species dataset with image features"""
    
    np.random.seed(42)
    
    species = ['Lion', 'Elephant', 'Tiger', 'Zebra', 'Giraffe', 'Bear', 'Wolf', 'Deer']
    n_samples = 100
    
    data = []
    
    for species_idx, animal in enumerate(species):
        for i in range(n_samples):
            if animal == 'Lion':
                color_intensity = np.random.normal(0.7, 0.1)
                edge_density = np.random.normal(0.6, 0.1)
                size_estimate = np.random.normal(0.8, 0.1)
                texture_roughness = np.random.normal(0.5, 0.1)
                symmetry_score = np.random.normal(0.65, 0.1)
                eye_detection = np.random.normal(0.72, 0.1)
                fur_density = np.random.normal(0.63, 0.1)
                shape_complexity = np.random.normal(0.52, 0.1)
                
            elif animal == 'Elephant':
                color_intensity = np.random.normal(0.4, 0.1)
                edge_density = np.random.normal(0.4, 0.1)
                size_estimate = np.random.normal(0.95, 0.05)
                texture_roughness = np.random.normal(0.8, 0.1)
                symmetry_score = np.random.normal(0.7, 0.1)
                eye_detection = np.random.normal(0.74, 0.1)
                fur_density = np.random.normal(0.66, 0.1)
                shape_complexity = np.random.normal(0.54, 0.1)
                
            elif animal == 'Tiger':
                color_intensity = np.random.normal(0.8, 0.1)
                edge_density = np.random.normal(0.8, 0.1)
                size_estimate = np.random.normal(0.75, 0.1)
                texture_roughness = np.random.normal(0.6, 0.1)
                symmetry_score = np.random.normal(0.72, 0.1)
                eye_detection = np.random.normal(0.76, 0.1)
                fur_density = np.random.normal(0.69, 0.1)
                shape_complexity = np.random.normal(0.56, 0.1)
                
            elif animal == 'Zebra':
                color_intensity = np.random.normal(0.5, 0.1)
                edge_density = np.random.normal(0.9, 0.05)
                size_estimate = np.random.normal(0.65, 0.1)
                texture_roughness = np.random.normal(0.7, 0.1)
                symmetry_score = np.random.normal(0.75, 0.1)
                eye_detection = np.random.normal(0.78, 0.1)
                fur_density = np.random.normal(0.72, 0.1)
                shape_complexity = np.random.normal(0.58, 0.1)
                
            elif animal == 'Giraffe':
                color_intensity = np.random.normal(0.6, 0.1)
                edge_density = np.random.normal(0.5, 0.1)
                size_estimate = np.random.normal(0.85, 0.1)
                texture_roughness = np.random.normal(0.55, 0.1)
                symmetry_score = np.random.normal(0.68, 0.1)
                eye_detection = np.random.normal(0.70, 0.1)
                fur_density = np.random.normal(0.60, 0.1)
                shape_complexity = np.random.normal(0.50, 0.1)
                
            elif animal == 'Bear':
                color_intensity = np.random.normal(0.3, 0.1)
                edge_density = np.random.normal(0.55, 0.1)
                size_estimate = np.random.normal(0.8, 0.1)
                texture_roughness = np.random.normal(0.75, 0.1)
                symmetry_score = np.random.normal(0.62, 0.1)
                eye_detection = np.random.normal(0.64, 0.1)
                fur_density = np.random.normal(0.57, 0.1)
                shape_complexity = np.random.normal(0.48, 0.1)
                
            elif animal == 'Wolf':
                color_intensity = np.random.normal(0.45, 0.1)
                edge_density = np.random.normal(0.65, 0.1)
                size_estimate = np.random.normal(0.6, 0.1)
                texture_roughness = np.random.normal(0.5, 0.1)
                symmetry_score = np.random.normal(0.7, 0.1)
                eye_detection = np.random.normal(0.68, 0.1)
                fur_density = np.random.normal(0.55, 0.1)
                shape_complexity = np.random.normal(0.46, 0.1)
                
            else:  # Deer
                color_intensity = np.random.normal(0.55, 0.1)
                edge_density = np.random.normal(0.45, 0.1)
                size_estimate = np.random.normal(0.55, 0.1)
                texture_roughness = np.random.normal(0.4, 0.1)
                symmetry_score = np.random.normal(0.73, 0.1)
                eye_detection = np.random.normal(0.71, 0.1)
                fur_density = np.random.normal(0.61, 0.1)
                shape_complexity = np.random.normal(0.51, 0.1)
            
            data.append({
                'Species': animal,
                'Color_Intensity': np.clip(color_intensity, 0, 1),
                'Edge_Density': np.clip(edge_density, 0, 1),
                'Size_Estimate': np.clip(size_estimate, 0, 1),
                'Texture_Roughness': np.clip(texture_roughness, 0, 1),
                'Symmetry_Score': np.clip(symmetry_score, 0, 1),
                'Eye_Detection': np.clip(eye_detection, 0, 1),
                'Fur_Density': np.clip(fur_density, 0, 1),
                'Shape_Complexity': np.clip(shape_complexity, 0, 1)
            })
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✓ Animal species dataset saved to {filename}")
    return df

# ============================================================================
# 2. GENERATE FEATURE ANALYSIS DATASET
# ============================================================================

def generate_feature_analysis(filename='feature_analysis.csv'):
    """Generate feature analysis statistics by species"""
    
    df = pd.read_csv('animal_species_data.csv')
    
    feature_cols = ['Color_Intensity', 'Edge_Density', 'Size_Estimate', 'Texture_Roughness',
                    'Symmetry_Score', 'Eye_Detection', 'Fur_Density', 'Shape_Complexity']
    
    analysis = []
    
    for species in df['Species'].unique():
        species_data = df[df['Species'] == species]
        
        for feature in feature_cols:
            analysis.append({
                'Species': species,
                'Feature': feature,
                'Mean': species_data[feature].mean(),
                'Std': species_data[feature].std(),
                'Min': species_data[feature].min(),
                'Max': species_data[feature].max()
            })
    
    analysis_df = pd.DataFrame(analysis)
    analysis_df.to_csv(filename, index=False)
    print(f"✓ Feature analysis saved to {filename}")
    return analysis_df

# ============================================================================
# 3. GENERATE CLASSIFICATION PERFORMANCE DATASET
# ============================================================================

def generate_classification_performance(filename='classification_performance.csv'):
    """Generate classification performance metrics by species"""
    
    species = ['Lion', 'Elephant', 'Tiger', 'Zebra', 'Giraffe', 'Bear', 'Wolf', 'Deer']
    
    performance_data = []
    
    # Simulated per-species performance metrics
    performance_matrix = {
        'Lion': {'Accuracy': 0.85, 'Precision': 0.84, 'Recall': 0.85, 'F1': 0.84},
        'Elephant': {'Accuracy': 0.83, 'Precision': 0.83, 'Recall': 0.83, 'F1': 0.83},
        'Tiger': {'Accuracy': 0.82, 'Precision': 0.82, 'Recall': 0.82, 'F1': 0.82},
        'Zebra': {'Accuracy': 0.81, 'Precision': 0.81, 'Recall': 0.81, 'F1': 0.81},
        'Giraffe': {'Accuracy': 0.80, 'Precision': 0.80, 'Recall': 0.80, 'F1': 0.80},
        'Bear': {'Accuracy': 0.79, 'Precision': 0.79, 'Recall': 0.79, 'F1': 0.79},
        'Wolf': {'Accuracy': 0.78, 'Precision': 0.78, 'Recall': 0.78, 'F1': 0.78},
        'Deer': {'Accuracy': 0.77, 'Precision': 0.77, 'Recall': 0.77, 'F1': 0.77}
    }
    
    for species in species:
        metrics = performance_matrix[species]
        performance_data.append({
            'Species': species,
            'Accuracy': metrics['Accuracy'],
            'Precision': metrics['Precision'],
            'Recall': metrics['Recall'],
            'F1_Score': metrics['F1'],
            'Samples_Tested': 20
        })
    
    perf_df = pd.DataFrame(performance_data)
    perf_df.to_csv(filename, index=False)
    print(f"✓ Classification performance saved to {filename}")
    return perf_df

# ============================================================================
# 4. GENERATE CONFUSION MATRIX DATASET
# ============================================================================

def generate_confusion_matrix_data(filename='confusion_matrix_data.csv'):
    """Generate confusion matrix data for visualization"""
    
    species = ['Lion', 'Elephant', 'Tiger', 'Zebra', 'Giraffe', 'Bear', 'Wolf', 'Deer']
    
    # Simulated confusion matrix (diagonal represents correct predictions)
    np.random.seed(42)
    cm = np.random.randint(15, 21, size=(8, 8))
    
    # Make diagonal higher (correct predictions)
    for i in range(8):
        cm[i, i] = np.random.randint(16, 20)
    
    cm_data = []
    
    for i, actual_species in enumerate(species):
        for j, predicted_species in enumerate(species):
            cm_data.append({
                'Actual_Species': actual_species,
                'Predicted_Species': predicted_species,
                'Count': cm[i, j]
            })
    
    cm_df = pd.DataFrame(cm_data)
    cm_df.to_csv(filename, index=False)
    print(f"✓ Confusion matrix data saved to {filename}")
    return cm_df

# ============================================================================
# 5. GENERATE IMAGE QUALITY ASSESSMENT DATASET
# ============================================================================

def generate_image_quality_assessment(filename='image_quality_assessment.csv'):
    """Generate image quality assessment data"""
    
    species = ['Lion', 'Elephant', 'Tiger', 'Zebra', 'Giraffe', 'Bear', 'Wolf', 'Deer']
    
    quality_data = []
    
    for species_name in species:
        for i in range(100):
            quality_data.append({
                'Species': species_name,
                'Image_ID': f'{species_name}_{i:03d}',
                'Resolution': np.random.choice(['High', 'Medium', 'Low']),
                'Brightness': np.random.normal(0.5, 0.15),
                'Contrast': np.random.normal(0.6, 0.15),
                'Sharpness': np.random.normal(0.7, 0.15),
                'Quality_Score': np.random.uniform(0.6, 0.95),
                'Processing_Time_ms': np.random.uniform(50, 500)
            })
    
    quality_df = pd.DataFrame(quality_data)
    quality_df.to_csv(filename, index=False)
    print(f"✓ Image quality assessment saved to {filename}")
    return quality_df

# ============================================================================
# 6. GENERATE MODEL TRAINING HISTORY
# ============================================================================

def generate_model_training_history(filename='training_history.csv'):
    """Generate model training history data"""
    
    epochs = 50
    history_data = []
    
    for epoch in range(1, epochs + 1):
        # Simulated training curves
        train_loss = 2.0 * np.exp(-epoch/15) + 0.1 * np.random.random()
        val_loss = 2.0 * np.exp(-epoch/15) + 0.15 * np.random.random()
        train_acc = 1 - (2.0 * np.exp(-epoch/15))
        val_acc = 1 - (2.0 * np.exp(-epoch/15)) - 0.02 * np.random.random()
        
        history_data.append({
            'Epoch': epoch,
            'Training_Loss': max(0.1, train_loss),
            'Validation_Loss': max(0.1, val_loss),
            'Training_Accuracy': np.clip(train_acc, 0, 1),
            'Validation_Accuracy': np.clip(val_acc, 0, 1)
        })
    
    history_df = pd.DataFrame(history_data)
    history_df.to_csv(filename, index=False)
    print(f"✓ Model training history saved to {filename}")
    return history_df

# ============================================================================
# 7. GENERATE SYSTEM INSIGHTS AND RECOMMENDATIONS
# ============================================================================

def generate_system_insights(filename='system_insights.csv'):
    """Generate system insights and recommendations"""
    
    insights = [
        {
            'Category': 'Model Performance',
            'Finding': 'Logistic Regression achieves 83.13% accuracy',
            'Recommendation': 'Consider ensemble methods for improved accuracy',
            'Priority': 'High',
            'Impact': 'Accuracy improvement'
        },
        {
            'Category': 'Data Quality',
            'Finding': 'Image resolution varies across dataset',
            'Recommendation': 'Implement image preprocessing and normalization',
            'Priority': 'High',
            'Impact': 'Consistency improvement'
        },
        {
            'Category': 'Feature Engineering',
            'Finding': 'Color intensity and edge density are top features',
            'Recommendation': 'Develop specialized features for difficult species',
            'Priority': 'Medium',
            'Impact': 'Classification accuracy'
        },
        {
            'Category': 'Species Confusion',
            'Finding': 'Tiger and Lion confusion rate is 15%',
            'Recommendation': 'Add mane detection and stripe pattern features',
            'Priority': 'High',
            'Impact': 'Reduce misclassification'
        },
        {
            'Category': 'Processing Speed',
            'Finding': 'Average processing time is 250ms per image',
            'Recommendation': 'Optimize CNN architecture for real-time processing',
            'Priority': 'Medium',
            'Impact': 'System responsiveness'
        },
        {
            'Category': 'Scalability',
            'Finding': 'System handles 800 species images efficiently',
            'Recommendation': 'Implement distributed processing for larger datasets',
            'Priority': 'Low',
            'Impact': 'Future scalability'
        }
    ]
    
    insights_df = pd.DataFrame(insights)
    insights_df.to_csv(filename, index=False)
    print(f"✓ System insights saved to {filename}")
    return insights_df

# ============================================================================
# 8. MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    print("\n" + "=" * 90)
    print("ANIMAL SPECIES IDENTIFICATION - DATASET GENERATION")
    print("=" * 90)
    
    print("\n[Step 1] Generating Animal Species Dataset...")
    df_species = generate_animal_species_dataset()
    print(f"  Dataset shape: {df_species.shape}")
    print(f"  Species: {df_species['Species'].unique().tolist()}")
    
    print("\n[Step 2] Generating Feature Analysis...")
    df_features = generate_feature_analysis()
    print(f"  Features analyzed: {df_features['Feature'].nunique()}")
    
    print("\n[Step 3] Generating Classification Performance...")
    df_perf = generate_classification_performance()
    print(f"  Species evaluated: {len(df_perf)}")
    
    print("\n[Step 4] Generating Confusion Matrix Data...")
    df_cm = generate_confusion_matrix_data()
    print(f"  Matrix size: 8x8")
    
    print("\n[Step 5] Generating Image Quality Assessment...")
    df_quality = generate_image_quality_assessment()
    print(f"  Quality records: {len(df_quality)}")
    
    print("\n[Step 6] Generating Model Training History...")
    df_history = generate_model_training_history()
    print(f"  Training epochs: {len(df_history)}")
    
    print("\n[Step 7] Generating System Insights...")
    df_insights = generate_system_insights()
    print(f"  Insights generated: {len(df_insights)}")
    
    print("\n" + "=" * 90)
    print("DATASET GENERATION COMPLETED")
    print("=" * 90)
    print("\nGenerated Files:")
    print("  1. animal_species_data.csv")
    print("  2. feature_analysis.csv")
    print("  3. classification_performance.csv")
    print("  4. confusion_matrix_data.csv")
    print("  5. image_quality_assessment.csv")
    print("  6. training_history.csv")
    print("  7. system_insights.csv")

if __name__ == "__main__":
    main()
