task=$1
llm=$2
test_llm=gpt-4o
datasets=("soybean" "wheat" "news")
methods=("rag" "graphrag" "raptor" "hypergrag")

results_dir=results/${llm}

if [ "$task" = "query" ]; then
    fname="query_llm.py"
    dir="configs"
elif [ "$task" = "query-rule" ]; then
    fname="query_llm.py"
    dir="configs/rules"
elif [ "$task" = "test" ]; then
    fname="test_answers.py"
    dir="configs"
    llm=$test_llm
elif [ "$task" = "test-rule" ]; then
    fname="test_answers.py"
    dir="configs/rules"
    llm=$test_llm
fi

for dataset in "${datasets[@]}"; do
    for method in "${methods[@]}"; do
        command="python ${fname} --config_file ${dir}/${method}/config_${dataset}.yaml --model.deployment_name ${llm} --results_dir ${results_dir}"
        if [ "$method" = "llm" ]; then
           echo "${command} $@";
           eval "${command} $@";
        elif [ "$method" = "rag" ]; then
           echo "${command} --query.hyperparams.top_k 2 $@";
           eval "${command} --query.hyperparams.top_k 2 $@";
           echo "${command} --query.hyperparams.top_k 5 $@";
           eval "${command} --query.hyperparams.top_k 5 $@";
        elif [ "$method" = "raptor" ]; then
           echo "${command} --query.hyperparams.similarity_top_k 2 $@";
           eval "${command} --query.hyperparams.similarity_top_k 2 $@";
           echo "${command} --query.hyperparams.similarity_top_k 5 $@";
           eval "${command} --query.hyperparams.similarity_top_k 5 $@";
        elif [ "$method" = "graphrag" ]; then
           echo "${command} --query.hyperparams.method local $@";
           eval "${command} --query.hyperparams.method local $@";
           echo "${command} --query.hyperparams.method global $@";
           eval "${command} --query.hyperparams.method global $@";
        elif [ "$method" = "hypergrag" ]; then
           echo "${command} --query.hyperparams.top_k 2 --query.hyperparams.nodes_top_k 5 $@";
           eval "${command} --query.hyperparams.top_k 2 --query.hyperparams.nodes_top_k 5 $@";
           echo "${command} --query.hyperparams.top_k 5 --query.hyperparams.nodes_top_k 10 $@";
           eval "${command} --query.hyperparams.top_k 5 --query.hyperparams.nodes_top_k 10 $@";
        fi
    done
done
