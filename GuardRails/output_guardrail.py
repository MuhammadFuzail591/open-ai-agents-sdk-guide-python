# This program will restricts the output to be less then 30 characters.

from agents import Agent, Runner, output_guardrail, GuardrailFunctionOutput, OutputGuardrailTripwireTriggered
from config.openai_config import config


@output_guardrail
def check_length(context, agent, output) -> GuardrailFunctionOutput:
   if len(output) > 3000:
      return GuardrailFunctionOutput(
         output_info="Output is Lengthy",
         tripwire_triggered= True
      )
   else:
      return GuardrailFunctionOutput(
         output_info="OUtput is Okay",
         tripwire_triggered= False
      )


agent = Agent(
   name="Text Gen Assistant",
   instructions="You are helpful assistant",
   output_guardrails = [check_length]
)


def output_guardrail_func():
   try:
      res = Runner.run_sync(agent, "Hi there, can you help me with the homework, I will provide you the details and you have to repsond accordingly",  run_config=config)
      print("Agent run smoothly",res.final_output )

   except OutputGuardrailTripwireTriggered:
      print("You have exceeded the max character limit of 30 chars. Try to limit your input to 30 characters..")



