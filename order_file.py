import pandas as pd

# Leia o arquivo readme.md
file_path = 'raw_readme.md'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Localize a linha do cabeçalho e o índice da tabela
header_index = None
for i, line in enumerate(lines):
    if line.startswith("| Title"):
        header_index = i
        break

# Separe o cabeçalho e as linhas da tabela
header = lines[header_index]
table_lines = lines[header_index + 2:]  # Pular a linha do cabeçalho e a linha de separação

# Leia a tabela para um DataFrame do Pandas
data = [line.strip().split('|')[1:-1] for line in table_lines]
columns = [col.strip() for col in header.strip().split('|')[1:-1]]
df = pd.DataFrame(data, columns=columns)

# Converta a coluna 'Published' para datetime e ordene
df['Published'] = pd.to_datetime(df['Published'])
df_sorted = df.sort_values(by='Published', ascending=False)

# Converta a coluna 'Published' de volta para strings
df_sorted['Published'] = df_sorted['Published'].dt.strftime('%Y-%m-%d')

# Escreva a tabela ordenada de volta para um novo arquivo
sorted_file_path = 'README.md'
with open(sorted_file_path, 'w') as file:
    file.write('# Useful Links\n\n')
    file.write('| ' + ' | '.join(columns) + ' |\n')
    file.write('| ' + ' | '.join(['---'] * len(columns)) + ' |\n')
    for _, row in df_sorted.iterrows():
        file.write('| ' + ' | '.join(row.astype(str)) + ' |\n')

print(f'Tabela ordenada salva em {sorted_file_path}')
