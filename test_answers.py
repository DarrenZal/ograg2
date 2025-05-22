from utils import create_service_context, get_config, load_llm_and_embeds
# from qna.tester import AspectTester, RAGASTester  # Missing qna module
import os

print("⚠️  The evaluation functionality (test_answers.py) requires the missing 'qna' module.")
print("   The main OG-RAG system works without it. Use query_llm.py for interactive queries.")
print("   If you need evaluation, the 'qna' testing module needs to be implemented.")

if __name__ == '__main__':
    print("Exiting - evaluation functionality requires missing 'qna' module.")
    exit(1)
    
    # The following code requires the missing 'qna' module:
    # config = get_config()
    # llm, embeddings = load_llm_and_embeds(config.model, config.embedding_model)
    # ... rest of evaluation code commented out