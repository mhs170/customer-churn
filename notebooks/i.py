project_root = os.getcwd()
path = os.path.join(project_root, "../data/cleaned.csv")
df = pd.read_csv(path)

cleaned_path = os.path.join(project_root, "../data/cleaned1.csv")
df.to_csv(cleaned_path, index=False)