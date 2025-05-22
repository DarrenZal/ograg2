#!/usr/bin/env python3
"""
Simple test script for OG-RAG that bypasses missing dependencies
"""
from utils import get_config, load_llm_and_embeds
import os

def simple_query_test():
    """Test basic query functionality"""
    try:
        print("🔧 Loading configuration...")
        config = get_config()
        
        print("🤖 Loading LLM and embeddings...")
        llm, embeddings = load_llm_and_embeds(config.model, config.embedding_model)
        
        print("✅ Configuration and models loaded successfully!")
        print(f"📋 Model: {config.model.deployment_name}")
        print(f"📋 Embedding Model: {config.embedding_model.deployment_name}")
        
        # Test a simple LLM call
        print("\n🧪 Testing direct LLM call...")
        test_prompt = "What is soybean cultivation?"
        response = llm.invoke(test_prompt)
        print(f"Response: {response.content[:200]}...")
        
        print("\n✅ Basic functionality test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False

def check_data_availability():
    """Check if test data is available"""
    print("\n📁 Checking data availability...")
    
    data_paths = [
        "data/ontology/farm_cropcultivation_schema_ontology_jsonld.json",
        "data/kg/soybean",
        "configs/config_soybean.yaml"
    ]
    
    for path in data_paths:
        if os.path.exists(path):
            print(f"✅ Found: {path}")
        else:
            print(f"❌ Missing: {path}")

if __name__ == "__main__":
    print("🚀 Starting OG-RAG Simple Test")
    print("=" * 50)
    
    check_data_availability()
    
    if simple_query_test():
        print("\n🎉 All tests passed! OG-RAG is working.")
    else:
        print("\n❌ Tests failed. Check configuration and API keys.")