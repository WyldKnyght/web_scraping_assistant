from sklearn.model_selection import train_test_split
import glob

def prepare_training_data():
    # Get the file paths of the preprocessed data
    preprocessed_data_paths = glob.glob("data/preprocessed_data/*.txt")

    # Create empty lists for the data and labels
    data = []
    labels = []

    # Iterate over the preprocessed data files
    for file_path in preprocessed_data_paths:
        # Read the preprocessed text from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Append the preprocessed text to the data list
        data.append(text)

        # Extract the label from the file name
        label = file_path.split("/")[-1].split("-")[0]

        # Append the label to the labels list
        labels.append(label)

    # Split the data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Return the training and validation data and labels
    return X_train, X_val, y_train, y_val
