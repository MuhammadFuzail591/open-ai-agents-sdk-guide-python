## Runner.run

#### -> It asynchronously run an agent until final output is produced.

#### -> It returns RunResult that includes conversation history, tool calls, handoffs and final output.

## Runner.run_sync

#### -> It synchronously run an agent until final output is produced.

#### -> The difference from the run is that it can do same task without async/await. Just call it and get your response directly.

## Runner.run_streamed

#### -> It asynchronously run an agent like Runner.run but give output token by token.

#### -> It returns RunResultStreaming that includes .stream_events() to get realtime output data (updates).

## Guardrails

## Streaming

## Sessions

## Tracing

## Context

## Tools

### Agent as a tool

#### -> custom_output_extractor : To modify the response of agent as tool.

## ------------- 2 Aug 2025 -----------------

## Function Tool properties (@function_tool)

#### -> name_override : str

#### -> description_override : str

#### -> use_docstring_info : Bool

### Handling Errors in function_tool

## enable_verbose_stdout_logging

## agents.exceptions

## Handoff

#### ->on_handoff
