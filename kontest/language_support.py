import os
import subprocess


class RunCmdGenerator:
    @staticmethod
    def python3(path, input_string):
        process = subprocess.Popen(
            ["python3", path],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate(input=input_string)
        print(stdout, stderr)
        process.wait()
        if process.returncode != 0:
            raise Exception(f"Error occurred: {stderr}")

        return "".join(stdout.split())

    @staticmethod
    def java(path, input_string):
        work_dir, _ = path.rsplit(os.sep, 1)
        if not os.path.exists(os.path.join(work_dir, 'Main.class')):
            os.rename(path, path.replace('script.file', 'Main.java'))
            path = path.replace('script.file', 'Main.java')
            compile_process = subprocess.Popen(
                ["javac", path],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir
            )
            stdout, stderr = compile_process.communicate()
            compile_process.wait()

            if compile_process.returncode != 0:
                raise Exception(f"Compilation error: {stderr}")

        run_process = subprocess.Popen(
            ["java", "Main"],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_dir
        )
        stdout, stderr = run_process.communicate(input_string)
        run_process.wait()

        if run_process.returncode != 0:
            raise Exception(f"Runtime error: {stderr}")

        return "".join(stdout.split())

    @staticmethod
    def cpp(path, input_string):
        work_dir, _ = path.rsplit(os.sep, 1)
        binary_name = "a.out"
        if not os.path.exists(os.path.join(work_dir, binary_name)):
            os.rename(path, path.replace('script.file', 'main.cpp'))
            compile_process = subprocess.Popen(
                ["g++", path.replace('script.file', 'main.cpp'), "-o", binary_name],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir
            )
            stdout, stderr = compile_process.communicate()
            compile_process.wait()

            if compile_process.returncode != 0:
                raise Exception(f"Compilation error: {stderr}")

        run_process = subprocess.Popen(
            [os.path.join(work_dir, binary_name)],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_dir
        )
        stdout, stderr = run_process.communicate(input=input_string)
        run_process.wait()

        if run_process.returncode != 0:
            raise Exception(f"Runtime error: {stderr}")

        return "".join(stdout.split())

    @staticmethod
    def c(path, input_string):
        work_dir, _ = path.rsplit(os.sep, 1)
        binary_name = "a.out"
        if not os.path.exists(os.path.join(work_dir, binary_name)):
            os.rename(path, path.replace('script.file', 'main.c'))
            compile_process = subprocess.Popen(
                ["gcc", path.replace('script.file', 'main.c'), "-o", binary_name],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir
            )
            stdout, stderr = compile_process.communicate()
            compile_process.wait()

            if compile_process.returncode != 0:
                raise Exception(f"Compilation error: {stderr}")

        run_process = subprocess.Popen(
            [os.path.join(work_dir, binary_name)],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_dir
        )
        stdout, stderr = run_process.communicate(input=input_string)
        run_process.wait()

        if run_process.returncode != 0:
            raise Exception(f"Runtime error: {stderr}")

        return "".join(stdout.split())

    @staticmethod
    def go(path, input_string):
        work_dir, _ = path.rsplit(os.sep, 1)
        binary_name = "main"
        if not os.path.exists(os.path.join(work_dir, binary_name)):
            os.rename(path, path.replace('script.file', 'main.go'))
            compile_process = subprocess.Popen(
                ["go", "build", "-o", binary_name, path.replace('script.file', 'main.go')],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir
            )
            stdout, stderr = compile_process.communicate()
            compile_process.wait()

            if compile_process.returncode != 0:
                raise Exception(f"Compilation error: {stderr}")

        run_process = subprocess.Popen(
            [os.path.join(work_dir, binary_name)],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=work_dir
        )
        stdout, stderr = run_process.communicate(input=input_string)
        run_process.wait()

        if run_process.returncode != 0:
            raise Exception(f"Runtime error: {stderr}")

        return "".join(stdout.split())
