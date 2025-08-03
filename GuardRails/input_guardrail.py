# This program will restricts the input to be less then 30 characters.
import asyncio
from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
from config.openai_config import config


@input_guardrail
def check_length(context, agent, input) -> GuardrailFunctionOutput:
   if len(input) > 3000:
      return GuardrailFunctionOutput(
         output_info="Input is Lengthy",
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
   input_guardrails=[check_length]
)


async def input_guardrail_func():
   try:
      res = await Runner.run(agent, "Hi there, can you help me with the homework, I will provide you the details and you have to repsond accordingly",  run_config=config)
      print("Agent run smoothly",res.final_output )

   except InputGuardrailTripwireTriggered:
      print("You have exceeded the max character limit of 30 chars. Try to limit your input to 30 characters..")



