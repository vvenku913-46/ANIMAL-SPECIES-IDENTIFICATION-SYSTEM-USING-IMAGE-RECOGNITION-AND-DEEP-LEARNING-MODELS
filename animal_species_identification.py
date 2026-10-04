"""
Animal Species Identification System Using Image Recognition and Deep Learning Models
Classifies animal species from images using CNNs and computer vision techniques
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# ============================================================================
# 1. GENERATE SYNTHETIC ANIMAL IMAGE FEATURE DATASET
# ============================================================================

def generate_animal_dataset(n_samples=800, random_state=42):
    """Generate synthetic animal image features dataset"""
    np.random.seed(random_state)
    
    # Animal species classes
    species = ['Lion', 'Elephant', 'Tiger', 'Zebra', 'Giraffe', 'Bear', 'Wolf', 'Deer']
    
    # Generate image features (simulating CNN extracted features)
    # In real scenario, these would be features from pre-trained CNN models
    
    # Create balanced dataset
    samples_per_class = n_samples // len(species)
    
    all_features = []
    all_labels = []
    
    for species_idx, animal in enumerate(species):
        # Generate species-specific feature patterns
        if animal == 'Lion':
            # Lion features: golden color, mane, large face
            color_intensity = np.random.normal(0.7, 0.1, samples_per_class)
            edge_density = np.random.normal(0.6, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.8, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.5, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.65, 0.1, samples_per_class)
            
        elif animal == 'Elephant':
            # Elephant features: gray color, large size, wrinkled texture
            color_intensity = np.random.normal(0.4, 0.1, samples_per_class)
            edge_density = np.random.normal(0.4, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.95, 0.05, samples_per_class)
            texture_roughness = np.random.normal(0.8, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.7, 0.1, samples_per_class)
            
        elif animal == 'Tiger':
            # Tiger features: orange with stripes, high contrast
            color_intensity = np.random.normal(0.8, 0.1, samples_per_class)
            edge_density = np.random.normal(0.8, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.75, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.6, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.72, 0.1, samples_per_class)
            
        elif animal == 'Zebra':
            # Zebra features: black and white stripes, high contrast
            color_intensity = np.random.normal(0.5, 0.1, samples_per_class)
            edge_density = np.random.normal(0.9, 0.05, samples_per_class)
            size_estimate = np.random.normal(0.65, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.7, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.75, 0.1, samples_per_class)
            
        elif animal == 'Giraffe':
            # Giraffe features: brown patches, long neck, tall
            color_intensity = np.random.normal(0.6, 0.1, samples_per_class)
            edge_density = np.random.normal(0.5, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.85, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.55, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.68, 0.1, samples_per_class)
            
        elif animal == 'Bear':
            # Bear features: dark color, thick texture, powerful build
            color_intensity = np.random.normal(0.3, 0.1, samples_per_class)
            edge_density = np.random.normal(0.55, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.8, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.75, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.62, 0.1, samples_per_class)
            
        elif animal == 'Wolf':
            # Wolf features: gray, lean, alert posture
            color_intensity = np.random.normal(0.45, 0.1, samples_per_class)
            edge_density = np.random.normal(0.65, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.6, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.5, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.7, 0.1, samples_per_class)
            
        else:  # Deer
            # Deer features: brown, slender, graceful
            color_intensity = np.random.normal(0.55, 0.1, samples_per_class)
            edge_density = np.random.normal(0.45, 0.1, samples_per_class)
            size_estimate = np.random.normal(0.55, 0.1, samples_per_class)
            texture_roughness = np.random.normal(0.4, 0.1, samples_per_class)
            symmetry_score = np.random.normal(0.73, 0.1, samples_per_class)
        
        # Additional features
        eye_detection = np.random.normal(0.7 + species_idx * 0.02, 0.1, samples_per_class)
        fur_density = np.random.normal(0.6 + species_idx * 0.03, 0.1, samples_per_class)
        shape_complexity = np.random.normal(0.5 + species_idx * 0.02, 0.1, samples_per_class)
        
        # Stack features
        features = np.column_stack([
            color_intensity, edge_density, size_estimate, texture_roughness,
            symmetry_score, eye_detection, fur_density, shape_complexity
        ])
        
        all_features.append(features)
        all_labels.extend([species_idx] * samples_per_class)
    
    X = np.vstack(all_features)
    y = np.array(all_labels)
    
    # Shuffle dataset
    shuffle_idx = np.random.permutation(len(X))
    X = X[shuffle_idx]
    y = y[shuffle_idx]
    
    print("=" * 90)
    print("ANIMAL SPECIES IDENTIFICATION SYSTEM - DATASET OVERVIEW")
    print("=" * 90)
    print(f"\nTotal Samples: {len(X)}")
    print(f"Number of Species: {len(species)}")
    print(f"Species Classes: {', '.join(species)}")
    print(f"\nSamples per Species: {samples_per_class}")
    print(f"Feature Dimensions: {X.shape[1]}")
    
    return X, y, species

# ============================================================================
# 2. VISUALIZATION FUNCTIONS
# ============================================================================

def visualize_species_distribution(y, species):
    """Visualize distribution of animal species in dataset"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    unique, counts = np.unique(y, return_counts=True)
    species_names = [species[i] for i in unique]
    colors = plt.cm.Set3(np.linspace(0, 1, len(species)))
    
    bars = ax.bar(species_names, counts, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax.set_title('Distribution of Animal Species in Dataset', fontweight='bold', fontsize=14)
    ax.set_xlabel('Animal Species', fontweight='bold')
    ax.set_ylabel('Number of Samples', fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/species_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Species distribution visualization saved")
    plt.close()

def visualize_feature_importance(feature_importance, feature_names):
    """Visualize feature importance from Random Forest model"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    indices = np.argsort(feature_importance)[::-1]
    colors = plt.cm.viridis(np.linspace(0, 1, len(feature_names)))
    
    bars = ax.bar(range(len(feature_names)), feature_importance[indices], 
                   color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    ax.set_title('Feature Importance for Animal Species Classification', fontweight='bold', fontsize=14)
    ax.set_xlabel('Features', fontweight='bold')
    ax.set_ylabel('Importance Score', fontweight='bold')
    ax.set_xticks(range(len(feature_names)))
    ax.set_xticklabels([feature_names[i] for i in indices], rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/feature_importance.png', dpi=300, bbox_inches='tight')
    print("✓ Feature importance visualization saved")
    plt.close()

def visualize_model_comparison(results):
    """Visualize model performance comparison"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    models = list(results.keys())
    accuracy = [results[m]['Accuracy'] for m in models]
    precision = [results[m]['Precision'] for m in models]
    recall = [results[m]['Recall'] for m in models]
    f1 = [results[m]['F1-Score'] for m in models]
    
    colors = ['#2E86AB', '#A23B72', '#F18F01']
    
    # Accuracy comparison
    axes[0, 0].bar(models, accuracy, color=colors, alpha=0.8, edgecolor='black')
    axes[0, 0].set_title('Accuracy Comparison', fontweight='bold', fontsize=12)
    axes[0, 0].set_ylabel('Accuracy Score')
    axes[0, 0].set_ylim([0, 1])
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Precision comparison
    axes[0, 1].bar(models, precision, color=colors, alpha=0.8, edgecolor='black')
    axes[0, 1].set_title('Precision Comparison', fontweight='bold', fontsize=12)
    axes[0, 1].set_ylabel('Precision Score')
    axes[0, 1].set_ylim([0, 1])
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Recall comparison
    axes[1, 0].bar(models, recall, color=colors, alpha=0.8, edgecolor='black')
    axes[1, 0].set_title('Recall Comparison', fontweight='bold', fontsize=12)
    axes[1, 0].set_ylabel('Recall Score')
    axes[1, 0].set_ylim([0, 1])
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # F1-Score comparison
    axes[1, 1].bar(models, f1, color=colors, alpha=0.8, edgecolor='black')
    axes[1, 1].set_title('F1-Score Comparison', fontweight='bold', fontsize=12)
    axes[1, 1].set_ylabel('F1-Score')
    axes[1, 1].set_ylim([0, 1])
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/model_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Model comparison visualization saved")
    plt.close()

def visualize_confusion_matrix(y_test, y_pred, species):
    """Visualize confusion matrix for best model"""
    cm = confusion_matrix(y_test, y_pred)
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=species,
                yticklabels=species, cbar_kws={'label': 'Count'}, ax=ax)
    
    ax.set_title('Confusion Matrix - Gradient Boosting Classifier', fontweight='bold', fontsize=14)
    ax.set_xlabel('Predicted Species', fontweight='bold')
    ax.set_ylabel('Actual Species', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/confusion_matrix.png', dpi=300, bbox_inches='tight')
    print("✓ Confusion matrix visualization saved")
    plt.close()

def visualize_classification_metrics(results):
    """Visualize detailed classification metrics"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    models = list(results.keys())
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    
    x = np.arange(len(models))
    width = 0.2
    
    for i, metric in enumerate(metrics):
        values = [results[m][metric] for m in models]
        ax.bar(x + i*width, values, width, label=metric, alpha=0.8, edgecolor='black')
    
    ax.set_title('Comprehensive Classification Metrics Comparison', fontweight='bold', fontsize=14)
    ax.set_ylabel('Score', fontweight='bold')
    ax.set_xlabel('Classification Models', fontweight='bold')
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(models)
    ax.legend()
    ax.set_ylim([0, 1])
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/classification_metrics.png', dpi=300, bbox_inches='tight')
    print("✓ Classification metrics visualization saved")
    plt.close()

# ============================================================================
# 3. MODEL BUILDING AND TRAINING
# ============================================================================

def train_models(X_train, X_test, y_train, y_test, species):
    """Train multiple classification models"""
    print("\n" + "=" * 90)
    print("MODEL TRAINING")
    print("=" * 90)
    
    results = {}
    models = {}
    predictions = {}
    feature_importance_dict = {}
    
    # Logistic Regression
    print("\nTraining Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    
    results['Logistic Regression'] = {
        'Accuracy': accuracy_score(y_test, y_pred_lr),
        'Precision': precision_score(y_test, y_pred_lr, average='weighted', zero_division=0),
        'Recall': recall_score(y_test, y_pred_lr, average='weighted', zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_lr, average='weighted', zero_division=0)
    }
    models['Logistic Regression'] = lr_model
    predictions['Logistic Regression'] = y_pred_lr
    
    # Random Forest
    print("Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    
    results['Random Forest'] = {
        'Accuracy': accuracy_score(y_test, y_pred_rf),
        'Precision': precision_score(y_test, y_pred_rf, average='weighted', zero_division=0),
        'Recall': recall_score(y_test, y_pred_rf, average='weighted', zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_rf, average='weighted', zero_division=0)
    }
    models['Random Forest'] = rf_model
    predictions['Random Forest'] = y_pred_rf
    feature_importance_dict['Random Forest'] = rf_model.feature_importances_
    
    # Gradient Boosting
    print("Training Gradient Boosting Classifier...")
    gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb_model.fit(X_train, y_train)
    y_pred_gb = gb_model.predict(X_test)
    
    results['Gradient Boosting'] = {
        'Accuracy': accuracy_score(y_test, y_pred_gb),
        'Precision': precision_score(y_test, y_pred_gb, average='weighted', zero_division=0),
        'Recall': recall_score(y_test, y_pred_gb, average='weighted', zero_division=0),
        'F1-Score': f1_score(y_test, y_pred_gb, average='weighted', zero_division=0)
    }
    models['Gradient Boosting'] = gb_model
    predictions['Gradient Boosting'] = y_pred_gb
    feature_importance_dict['Gradient Boosting'] = gb_model.feature_importances_
    
    return results, models, predictions, y_pred_gb, feature_importance_dict

# ============================================================================
# 4. MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    print("\n" + "=" * 90)
    print("ANIMAL SPECIES IDENTIFICATION SYSTEM")
    print("=" * 90)
    
    # Generate dataset
    print("\n[Step 1] Generating Animal Image Features Dataset...")
    X, y, species = generate_animal_dataset(n_samples=800)
    
    # Prepare data for modeling
    print("\n[Step 2] Preparing Data for Modeling...")
    feature_names = ['Color Intensity', 'Edge Density', 'Size Estimate', 'Texture Roughness',
                     'Symmetry Score', 'Eye Detection', 'Fur Density', 'Shape Complexity']
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split data
    print("\n[Step 3] Splitting Data...")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)
    print(f"Training set size: {len(X_train)} samples")
    print(f"Test set size: {len(X_test)} samples")
    
    # Generate visualizations
    print("\n[Step 4] Generating Visualizations...")
    print("Creating species distribution...")
    visualize_species_distribution(y, species)
    
    # Train models
    print("\n[Step 5] Training Classification Models...")
    results, models, predictions, y_pred_gb, feature_importance_dict = train_models(
        X_train, X_test, y_train, y_test, species
    )
    
    # Print results
    print("\n" + "=" * 90)
    print("MODEL PERFORMANCE RESULTS")
    print("=" * 90)
    for model_name, metrics in results.items():
        print(f"\n{model_name}:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    # Generate additional visualizations
    print("\n[Step 6] Generating Additional Visualizations...")
    print("Creating feature importance...")
    visualize_feature_importance(feature_importance_dict['Gradient Boosting'], feature_names)
    
    print("Creating model comparison...")
    visualize_model_comparison(results)
    
    print("Creating confusion matrix...")
    visualize_confusion_matrix(y_test, y_pred_gb, species)
    
    print("Creating classification metrics...")
    visualize_classification_metrics(results)
    
    print("\n" + "=" * 90)
    print("EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 90)
    print("\nGenerated Visualizations:")
    print("  1. species_distribution.png")
    print("  2. feature_importance.png")
    print("  3. model_comparison.png")
    print("  4. confusion_matrix.png")
    print("  5. classification_metrics.png")
    
    return X, y, species, X_train, X_test, y_train, y_test, results, models

if __name__ == "__main__":
    X, y, species, X_train, X_test, y_train, y_test, results, models = main()
