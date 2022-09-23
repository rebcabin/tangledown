from ipykernel.ipkernel import IPythonKernel
from pprint import pprint
import sys  # for version_info
from pathlib import Path
from tangledown import \
        accumulate_lines, \
        get_lines, \
        expand_tangles


class TangledownKernel(IPythonKernel):
    current_victim_filepath = ""
    with open(Path.home() / '.tangledown/current_victim_file.txt') as v:
        fp = v.read()
    tracer_, nowebs, tangles_ = accumulate_lines(*get_lines(fp))
    implementation = 'Tangledown'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {  # for syntax coloring
        "name": "python",
        "version": sys.version.split()[0],
        "mimetype": "text/x-python",
        "codemirror_mode": {"name": "ipython", "version": sys.version_info[0]},
        "pygments_lexer": "ipython%d" % 3,
        "nbconvert_exporter": "python",
        "file_extension": ".py",
    }
    banner = "Tangledown kernel - expanding 'block' tags"
    
    
    async def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            cleaned_lines = [line + '\n' for line in code.split('\n')]
            # HERE'S THE BEEF!
            expanded_code = expand_tangles(None, [cleaned_lines], self.nowebs)
            reply_content = await super().do_execute(
                expanded_code, silent, store_history, user_expressions)
            stream_content = {
                'name': 'stdout',
                'text': reply_content,
            }
            self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=TangledownKernel)


