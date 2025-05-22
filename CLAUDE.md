# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

OG-RAG (Ontology-Grounded Retrieval Augmented Generation) is a Microsoft research project that enhances traditional RAG systems by incorporating domain-specific ontologies through hypergraph representations. The system compares multiple retrieval approaches across specialized domains like agriculture and healthcare.

## Core Architecture

### Main Components

**Knowledge Graph Module (`knowledge_graph/`)**
- Generates knowledge graph triples from ontology mappings
- Creates hypergraph representations for enhanced retrieval

**Ontology Mapping (`ontology_mapping/`)**  
- Maps domain documents to ontology concepts using LLMs
- Processes JSON-LD ontology schemas into document-concept mappings

**Query Engines (`query_engine/`)**
- Multiple retrieval strategies: OG-RAG hypergraph, traditional RAG, GraphRAG, RAPTOR, direct LLM
- Each engine implements different retrieval and generation approaches

**Configuration System**
- YAML-based configs with sections: model, embedding_model, data, query, evaluator
- Supports OpenAI/Azure models, multiple embedding providers, various datasets

## Common Commands

### Knowledge Graph Building
```bash
python build_knowledge_graph.py --config_file configs/<dataset>/config_<dataset>.yaml
```

### Interactive Querying
```bash
python query_llm.py --config_file configs/<dataset>/config_<dataset>.yaml
```

### Batch Evaluation
```bash
python test_answers.py --config_file configs/<dataset>/config_<dataset>.yaml
```

### Automation Scripts
```bash
./run_all.sh                    # Run all methods across all datasets
./run_method.sh <method>        # Run specific method across datasets  
./run_method_dataset.sh <method> <dataset>  # Run on specific dataset
```

## Query Methods

Available in config `query.method`:
- `ontohypergraph-rag`: Main OG-RAG implementation with hypergraph retrieval
- `rag`: Traditional vector-based RAG
- `graphrag`: Microsoft GraphRAG implementation
- `raptor-rag`: RAPTOR clustering-based retrieval
- `llm`: Direct LLM querying without retrieval
- `snippet-rag`: Snippet-based retrieval
- `full-onto`: Full ontology context retrieval

## Data Structure

**Dataset Organization**: `data/kg/{dataset}/`
- Ontology files as numbered JSON-LD files in `ontology/` subdirectory
- Knowledge graph triples stored as pickle files
- Vector embeddings and document stores

**Supported Datasets**: soybean, wheat, news, indiampop

## Development Notes

- Document loading supports PDF and Markdown with intelligent chunking
- Vector indices are created automatically and cached
- All LLM calls are configurable through YAML configs
- Evaluation uses RAGAS framework with custom metrics
- The system is designed for comparing different RAG approaches systematically