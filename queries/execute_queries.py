import os
import argparse

def main(args):
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)  # AlphaTrans 根目录

    databases_path = os.path.join(project_root, 'databases')
    data_path = os.path.join(project_root, 'data', args.output_path, args.project_name)

    os.makedirs(data_path, exist_ok=True)

    if args.query_name == 'get_imports':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_imports.ql | tail -n +3 >> {data_path}/{args.project_name}_imports.txt")

    if args.query_name == 'get_method_call_graph':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_method_call_graph_1.ql | tail -n +3 >> {data_path}/{args.project_name}_method_call_graph.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_method_call_graph_2.ql | tail -n +3 >> {data_path}/{args.project_name}_method_call_graph.txt")

    if args.query_name == 'get_constructor_call_graph':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_constructor_call_graph_1.ql | tail -n +3 >> {data_path}/{args.project_name}_constructor_call_graph.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_constructor_call_graph_2.ql | tail -n +3 >> {data_path}/{args.project_name}_constructor_call_graph.txt")

    if args.query_name == 'get_all_constructors':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_all_constructors_1.ql | tail -n +3 >> {data_path}/{args.project_name}_all_constructors.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_all_constructors_2.ql | tail -n +3 >> {data_path}/{args.project_name}_all_constructors.txt")

    if args.query_name == 'get_all_methods':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_all_methods_1.ql | tail -n +3 >> {data_path}/{args.project_name}_all_methods.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_all_methods_2.ql | tail -n +3 >> {data_path}/{args.project_name}_all_methods.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_all_methods_3.ql | tail -n +3 >> {data_path}/{args.project_name}_all_methods.txt")

    if args.query_name == 'get_fields':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_fields_1.ql | tail -n +3 >> {data_path}/{args.project_name}_fields.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_fields_2.ql | tail -n +3 >> {data_path}/{args.project_name}_fields.txt")

    if args.query_name == 'get_interfaces':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_interfaces_1.ql | tail -n +3 >> {data_path}/{args.project_name}_interfaces.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_interfaces_2.ql | tail -n +3 >> {data_path}/{args.project_name}_interfaces.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_interfaces_3.ql | tail -n +3 >> {data_path}/{args.project_name}_interfaces.txt")

    if args.query_name == 'get_nested_classes':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_nested_classes.ql | tail -n +3 >> {data_path}/{args.project_name}_nested_classes.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_nested_interfaces.ql | tail -n +3 >> {data_path}/{args.project_name}_nested_classes.txt")

    if args.query_name == 'get_superclasses':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_superclasses_1.ql | tail -n +3 >> {data_path}/{args.project_name}_superclasses.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_superclasses_2.ql | tail -n +3 >> {data_path}/{args.project_name}_superclasses.txt")

    if args.query_name == 'get_parameters':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_parameters_1.ql | tail -n +3 >> {data_path}/{args.project_name}_parameters.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_parameters_2.ql | tail -n +3 >> {data_path}/{args.project_name}_parameters.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_parameters_3.ql | tail -n +3 >> {data_path}/{args.project_name}_parameters.txt")

    if args.query_name == 'get_class_callables':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_class_callables_1.ql | tail -n +3 >> {data_path}/{args.project_name}_class_callables.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_class_callables_2.ql | tail -n +3 >> {data_path}/{args.project_name}_class_callables.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_class_callables_3.ql | tail -n +3 >> {data_path}/{args.project_name}_class_callables.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_class_callables_4.ql | tail -n +3 >> {data_path}/{args.project_name}_class_callables.txt")
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_class_callables_5.ql | tail -n +3 >> {data_path}/{args.project_name}_class_callables.txt")

    if args.query_name == 'get_call_graph':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_call_graph.ql | tail -n +3 >> {data_path}/{args.project_name}_call_graph.txt")

    if args.query_name == 'get_types':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_types.ql | tail -n +3 >> {data_path}/{args.project_name}_types.txt")

    if args.query_name == 'get_overridden_methods':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_overridden_methods.ql | tail -n +3 >> {data_path}/{args.project_name}_overridden_methods.txt")

    if args.query_name == 'get_static_initializers':
        os.system(f"codeql query run -d {databases_path}/{args.database_name} -- {script_dir}/get_static_initializers.ql | tail -n +3 >> {data_path}/{args.project_name}_static_initializers.txt")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='execute codeql queries')
    parser.add_argument('--project_name', type=str, help='Project name to simplify', required=True)
    parser.add_argument('--query_name', type=str, help='Query name to execute', required=True)
    parser.add_argument('--database_name', type=str, help='Database name to execute', required=True)
    parser.add_argument('--output_path', type=str, help='Output path to save the results', required=True)
    args = parser.parse_args()
    main(args)
