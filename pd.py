from perfetto.trace_processor import TraceProcessor

filename = 'trace_836c2a8b-716f-42ed-a510-5edfb01e8fcc.perfetto'
# Initialise TraceProcessor with a trace file
tp = TraceProcessor(file_path=filename)
