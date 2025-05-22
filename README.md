# Ontology Generated Retrieval Augmented Generation (OG-RAG)
![OG-RAG: Ontology-Grounded Retrieval-Augmented Generation](https://arxiv.org/html/2412.15235v1/x1.png)

**OG-RAG** enhances Large Language Models (LLMs) with domain-specific ontologies for improved factual accuracy and contextually relevant responses in fields with specialized workflows like agriculture, healthcare, knowledge work, and more.

[**Paper:** OG-RAG: Ontology-Grounded Retrieval-Augmented Generation For Large Language Models](https://arxiv.org/html/2412.15235v1)

---

## 🔍 Overview
![OG-RAG Flow](https://arxiv.org/html/2412.15235v1/x2.png)

OG-RAG addresses traditional Retrieval-Augmented Generation (RAG) limitations by using hypergraphs to incorporate ontology-grounded knowledge. It retrieves minimal, highly relevant contexts, significantly boosting response accuracy and factual grounding.

---

## 📈 Key Features

* **Ontology-Grounded Retrieval**
* **Hypergraph Context Representation**
* **Optimized Context Retrieval Algorithm**
* **Enhanced Factual Accuracy**

---

## 🛠️ Installation

### Standard Installation

```bash
git clone https://github.com/yourusername/og-rag.git
cd og-rag
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Apple Silicon (M1/M2/M3) Installation

Due to dependency conflicts with Azure ML packages on Apple Silicon, use this alternative installation:

```bash
git clone https://github.com/yourusername/og-rag.git
cd og-rag
python3 -m venv venv
source venv/bin/activate

# Install core packages first
pip install openai llama-index langchain ragas pandas numpy pyyaml tiktoken easydict

# Install additional LlamaIndex packages
pip install llama-index-embeddings-langchain llama-index-llms-langchain
pip install llama-index-packs-raptor matplotlib ipython

# Copy and configure
cp configs/config_soybean.yaml.example configs/config_soybean.yaml
# Edit configs/config_soybean.yaml with your actual API key
```

**Note:** Replace `your-api-key-here` with your actual OpenAI API key.

---

## ⚙️ Configuration

### Step 1: Copy and Configure

```bash
# Copy the example configuration file
cp configs/config_soybean.yaml.example configs/config_soybean.yaml

# Edit the config file with your API key
# Change YOUR_OPENAI_API_KEY_HERE to your actual OpenAI API key
```

### Step 2: Your Configuration File

Edit `configs/config_soybean.yaml` with your preferences:

```yaml
model:
  api_base: 
  api_key: YOUR_OPENAI_API_KEY_HERE  # Replace with your actual API key
  deployment_name: gpt-4o
  api_type: openai
  api_version: '2024-02-01'

embedding_model:
  api_base: 
  api_key: YOUR_OPENAI_API_KEY_HERE  # Replace with your actual API key
  deployment_name: text-embedding-3-small
  api_type: openai
  api_version: '2024-02-01'

data:
  documents_dir: data/md/soybean
  ontology_path: data/ontology/farm_cropcultivation_schema_ontology_jsonld.json
  kg_storage_path: data/kg/soybean
  index_dir: index_openai/vector_soybean
  subdir: False
  smart_pdf: True
  chunk_size: 8192

query:
  framework: ontohypergraph-rag
  batch_size: 10
  mode: json
  questions_file:

question_generator:
  framework: ontodocragas
  test_size: 100
  distr:
    simple: 0
    reasoning: 1
    multi_context: 0

evaluator:
  eval_file:
  reference_free: True
  type: single
  metrics:
    - answer_correctness
    - faithfulness
    - answer_similarity
    - answer_relevancy
    - context_relevancy
    - context_precision
    - context_recall
    - context_entity_recall
```

## 🚀 Usage

### Quick Start Testing

Before running the full system, test basic functionality:

```bash
# Activate virtual environment
source venv/bin/activate

# Test core functionality (recommended first step)
python simple_test.py --config_file configs/config_soybean.yaml
```

### Interactive Querying

Execute interactive queries with the OG-RAG system:

```bash
python query_llm.py --config_file configs/config_soybean.yaml
```

This launches an interactive session where you can ask questions about soybean cultivation and see how the ontology-grounded system responds.

### Knowledge Graph Building

Map ontology and generate knowledge graph (required before first use):

```bash
python build_knowledge_graph.py --config_file configs/config_soybean.yaml
```

### Comprehensive Evaluation

Run full evaluation with RAGAS metrics:

```bash
python test_answers.py --config_file configs/config_soybean.yaml
```

### Batch Testing

Run multiple methods across datasets:

```bash
# Test all methods on all datasets
./run_all.sh

# Test specific method
./run_method.sh query gpt-4o ontohypergraph-rag

# Test on specific dataset
./run_method_dataset.sh query gpt-4o ontohypergraph-rag soybean
```

### Available Test Datasets

- `soybean` - Agriculture/farming knowledge
- `wheat` - Crop cultivation
- `news` - General news articles  
- `indiampop` - India population data

### Query Methods

Available methods for comparison:

- `ontohypergraph-rag` - Main OG-RAG implementation (recommended)
- `rag` - Traditional vector-based RAG
- `graphrag` - Microsoft GraphRAG
- `raptor-rag` - RAPTOR clustering-based retrieval
- `llm` - Direct LLM querying without retrieval

---

## 🔧 Troubleshooting

### Common Issues

**Azure ML Import Errors on Apple Silicon:**
- Use the Apple Silicon installation method above
- The system gracefully handles missing Azure ML dependencies

**Missing API Keys Error:**
- Copy example config: `cp configs/config_soybean.yaml.example configs/config_soybean.yaml`
- Edit `configs/config_soybean.yaml` and replace `YOUR_OPENAI_API_KEY_HERE` with your actual API key

**Model Not Found Errors:**
- Update model names in configs (e.g., `gpt-4o` instead of `gpt-4-32k`)
- Check your OpenAI account has access to the specified models

**Document Directory Missing:**
- The system expects documents in `data/md/{dataset}/`
- Sample documents are provided for testing

**F-string Syntax Errors:**
- These have been fixed in the codebase for Python compatibility

### Getting Help

1. Start with the simple test: `python simple_test.py`
2. Check the CLAUDE.md file for development guidance
3. Verify all dependencies are installed correctly

---

## 📚 Reference

* [**Paper:** OG-RAG: Ontology-Grounded Retrieval-Augmented Generation For Large Language Models](https://arxiv.org/html/2412.15235v1)



## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.