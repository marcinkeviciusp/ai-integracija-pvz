# OpenRouter Python SDK

The OpenRouter Python SDK is a type-safe toolkit for building AI applications with access to 300+ language models through a unified API. It provides automatic access to models from OpenAI, Anthropic, Google, Meta, Mistral, and many other providers through a single integration, eliminating the need to manage multiple provider-specific SDKs and API formats.

The SDK is auto-generated from OpenRouter's OpenAPI specifications and updated with every API change, ensuring new models and features are immediately available. All parameters, response fields, and configuration options are fully typed with Python type hints and validated with Pydantic, catching invalid configurations at runtime with clear error messages. The SDK supports both synchronous and asynchronous operations, streaming responses, and includes built-in resource management through context managers.

## Installation

```bash
# Using pip
pip install openrouter

# Using uv (recommended)
uv add openrouter

# Using poetry
poetry add openrouter
```

## Chat Completions - Send Chat Messages

The primary method for interacting with language models. Sends a request for a model response for a given chat conversation, supporting both streaming and non-streaming modes. Accepts messages in the standard chat format with roles (user, assistant, system) and returns model completions with usage metadata.

```python
from openrouter import OpenRouter
import os

# Basic chat completion
with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    response = client.chat.send(
        model="anthropic/claude-3.5-sonnet",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum computing in simple terms."}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    print(response.choices[0].message.content)

# Streaming chat completion
with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    response = client.chat.send(
        model="openai/gpt-4",
        messages=[{"role": "user", "content": "Write a short poem about Python."}],
        stream=True
    )
    with response as event_stream:
        for event in event_stream:
            if event.choices and event.choices[0].delta.content:
                print(event.choices[0].delta.content, end="", flush=True)

# Chat with provider preferences and zero data retention
with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    response = client.chat.send(
        model="anthropic/claude-3.5-sonnet",
        messages=[{"role": "user", "content": "Hello!"}],
        provider={
            "zdr": True,           # Zero data retention
            "sort": "price",       # Sort by price
            "order": ["anthropic", "openai"]  # Provider preference order
        }
    )
```

## Async Chat Completions - Asynchronous Requests

The SDK supports asynchronous operations for high-performance applications. Use `send_async` for non-blocking requests that can be awaited, ideal for web applications, batch processing, or when making multiple concurrent API calls.

```python
import asyncio
from openrouter import OpenRouter
import os

async def main():
    async with OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY", ""),
    ) as client:
        # Single async request
        response = await client.chat.send_async(
            model="anthropic/claude-3.5-sonnet",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.choices[0].message.content)

        # Async streaming
        response = await client.chat.send_async(
            model="openai/gpt-4",
            messages=[{"role": "user", "content": "Write a haiku about coding."}],
            stream=True
        )
        async with response as event_stream:
            async for event in event_stream:
                if event.choices and event.choices[0].delta.content:
                    print(event.choices[0].delta.content, end="")

asyncio.run(main())
```

## Completions - Text Completions

Creates a completion for the provided prompt using the legacy completions API. Useful for text generation tasks where you provide a prompt and receive a continuation. Supports streaming and various generation parameters like temperature and top_p.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    response = client.completions.generate(
        model="openai/gpt-3.5-turbo-instruct",
        prompt="Once upon a time in a land far away,",
        max_tokens=200,
        temperature=0.8,
        stream=False
    )
    print(response.choices[0].text)
```

## Beta Responses API - OpenResponses Format

Creates streaming or non-streaming responses using the OpenResponses API format. This beta endpoint provides enhanced features including reasoning configuration, tool calls, and multimodal outputs.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Basic response
    response = client.beta.responses.send(
        model="anthropic/claude-3.5-sonnet",
        input=[{"role": "user", "content": "What is the capital of France?"}],
        service_tier="auto",
        stream=False
    )
    with response as event_stream:
        for event in event_stream:
            print(event)

    # With reasoning and tools
    response = client.beta.responses.send(
        model="openai/gpt-4",
        input=[{"role": "user", "content": "Calculate 25 * 47"}],
        reasoning={"summary": "auto", "enabled": True},
        tools=[{
            "type": "function",
            "function": {
                "name": "calculator",
                "description": "Performs arithmetic calculations",
                "parameters": {"type": "object", "properties": {"expression": {"type": "string"}}}
            }
        }],
        temperature=0.5
    )
```

## Models - List Available Models

Retrieve information about all available models including their pricing, context length, capabilities, and supported parameters. Filter by category or get models available to a specific user based on their provider preferences.

```python
from openrouter import OpenRouter, operations
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # List all models
    models = client.models.list()
    for model in models.data:
        print(f"{model.id}: {model.name}")
        print(f"  Context: {model.context_length} tokens")
        print(f"  Pricing: ${model.pricing.prompt}/1K prompt, ${model.pricing.completion}/1K completion")

    # Get model count
    count = client.models.count()
    print(f"Total models available: {count.data.count}")

    # Filter by category
    programming_models = client.models.list(category="programming")

    # List models for authenticated user (with provider preferences applied)
    user_models = client.models.list_for_user(
        security=operations.ListModelsUserSecurity(
            bearer=os.getenv("OPENROUTER_BEARER", "")
        )
    )
```

## Embeddings - Generate Text Embeddings

Submit text to embedding models and receive vector representations. Useful for semantic search, clustering, and similarity comparisons. Supports batch inputs and configurable output formats.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Generate embeddings for text
    response = client.embeddings.generate(
        input="The quick brown fox jumps over the lazy dog.",
        model="openai/text-embedding-ada-002"
    )
    embedding = response.data[0].embedding
    print(f"Embedding dimension: {len(embedding)}")

    # Batch embeddings
    response = client.embeddings.generate(
        input=["First sentence", "Second sentence", "Third sentence"],
        model="openai/text-embedding-ada-002",
        encoding_format="float"
    )
    for i, item in enumerate(response.data):
        print(f"Text {i}: {len(item.embedding)} dimensions")

    # List available embedding models
    embedding_models = client.embeddings.list_models()
    for model in embedding_models.data:
        print(f"Embedding model: {model.id}")
```

## API Keys - Key Management

Manage API keys programmatically including listing, creating, updating, and deleting keys. Requires a provisioning key for most operations. Supports setting spending limits and reset intervals.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Get current key information
    current_key = client.api_keys.get_current_key_metadata()
    print(f"Label: {current_key.data.label}")
    print(f"Usage: ${current_key.data.usage}")
    print(f"Limit: ${current_key.data.limit}")
    print(f"Remaining: ${current_key.data.limit_remaining}")

    # List all API keys (requires provisioning key)
    keys = client.api_keys.list(include_disabled="false", offset="0")
    for key in keys.data:
        print(f"{key.name}: {key.hash[:16]}... Usage: ${key.usage}")

    # Create a new API key
    new_key = client.api_keys.create(
        name="Production API Key",
        limit=100.0,
        limit_reset="monthly",
        include_byok_in_limit=True
    )
    print(f"New key created: {new_key.key}")

    # Update an API key
    updated = client.api_keys.update(
        hash="f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943",
        name="Updated Key Name",
        limit=150.0,
        disabled=False
    )

    # Delete an API key
    result = client.api_keys.delete(
        hash="f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943"
    )
    print(f"Deleted: {result.deleted}")
```

## Credits - Account Balance

Get total credits purchased and usage information for the authenticated user. Includes crypto payment integration through Coinbase.

```python
from openrouter import OpenRouter, operations
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Get credit balance
    credits = client.credits.get_credits()
    print(f"Total Credits: ${credits.data.total_credits}")
    print(f"Total Usage: ${credits.data.total_usage}")
    print(f"Remaining: ${credits.data.total_credits - credits.data.total_usage}")

    # Create Coinbase charge for crypto payment
    charge = client.credits.create_coinbase_charge(
        security=operations.CreateCoinbaseChargeSecurity(
            bearer=os.getenv("OPENROUTER_BEARER", "")
        ),
        amount=100,
        sender="0x1234567890123456789012345678901234567890",
        chain_id=1
    )
    print(f"Charge ID: {charge.data.id}")
```

## Generations - Request History

Get metadata and usage information for past generation requests. Useful for debugging, cost tracking, and analytics.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Get generation details by ID
    generation = client.generations.get_generation(id="gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG")
    print(f"Model: {generation.data.model}")
    print(f"Provider: {generation.data.provider_name}")
    print(f"Cost: ${generation.data.total_cost}")
    print(f"Latency: {generation.data.latency}ms")
    print(f"Tokens - Prompt: {generation.data.tokens_prompt}, Completion: {generation.data.tokens_completion}")
    print(f"Finish Reason: {generation.data.finish_reason}")
```

## Providers - List AI Providers

Get information about all available AI providers including their names, slugs, and privacy policies.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    providers = client.providers.list()
    for provider in providers.data:
        print(f"{provider.name} ({provider.slug})")
        print(f"  Privacy Policy: {provider.privacy_policy_url}")
```

## Endpoints - Model Endpoint Information

Get detailed information about model endpoints including latency, throughput, and availability metrics. Preview the impact of Zero Data Retention (ZDR) on available endpoints.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # List endpoints for a specific model
    endpoints = client.endpoints.list(author="openai", slug="gpt-4")
    print(f"Model: {endpoints.data.name}")
    for endpoint in endpoints.data.endpoints:
        print(f"  {endpoint.provider_name}:")
        print(f"    Context: {endpoint.context_length}")
        print(f"    Uptime (30m): {endpoint.uptime_last_30m}%")
        print(f"    Latency p50: {endpoint.latency_last_30m.p50}ms")

    # Preview ZDR impact on endpoints
    zdr_endpoints = client.endpoints.list_zdr_endpoints()
    print(f"ZDR-compatible endpoints: {len(zdr_endpoints.data)}")
```

## Analytics - Usage Activity

Get user activity data grouped by endpoint for analytics and monitoring. Returns usage information for the last 30 days.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Get activity for a specific date
    activity = client.analytics.get_user_activity(date_="2025-01-15")
    for item in activity.data:
        print(f"Date: {item.date}")
        print(f"  Model: {item.model}")
        print(f"  Provider: {item.provider_name}")
        print(f"  Requests: {item.requests}")
        print(f"  Usage: ${item.usage}")
        print(f"  Tokens: {item.prompt_tokens + item.completion_tokens}")
```

## Guardrails - Usage Policies

Create and manage guardrails to control API usage with spending limits, allowed models, and provider restrictions. Assign guardrails to API keys or organization members.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # List guardrails
    guardrails = client.guardrails.list()
    for g in guardrails.data:
        print(f"{g.name} (ID: {g.id})")

    # Create a guardrail
    new_guardrail = client.guardrails.create(
        name="Production Guardrail",
        description="Limit production API usage",
        limit_usd=100.0,
        reset_interval="monthly",
        allowed_providers=["openai", "anthropic"],
        allowed_models=["openai/gpt-4", "anthropic/claude-3.5-sonnet"],
        enforce_zdr=True
    )
    guardrail_id = new_guardrail.data.id

    # Assign keys to guardrail
    client.guardrails.bulk_assign_keys(
        id=guardrail_id,
        key_hashes=["c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"]
    )

    # Assign members to guardrail
    client.guardrails.bulk_assign_members(
        id=guardrail_id,
        member_user_ids=["user_abc123", "user_def456"]
    )

    # Update guardrail
    client.guardrails.update(
        id=guardrail_id,
        limit_usd=150.0,
        name="Updated Production Guardrail"
    )

    # Delete guardrail
    client.guardrails.delete(id=guardrail_id)
```

## OAuth - Authentication Flow

Implement OAuth authentication flows to generate user-controlled API keys. Supports PKCE for enhanced security.

```python
from openrouter import OpenRouter
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    # Create authorization code (initiate OAuth flow)
    auth_response = client.o_auth.create_auth_code(
        callback_url="https://myapp.com/auth/callback",
        code_challenge="E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
        code_challenge_method="S256",
        limit=100.0
    )
    print(f"Auth Code ID: {auth_response.data.id}")
    # Redirect user to OpenRouter authorization page

    # Exchange authorization code for API key (after callback)
    key_response = client.o_auth.exchange_auth_code_for_api_key(
        code="auth_code_abc123def456",
        code_verifier="dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
        code_challenge_method="S256"
    )
    print(f"User API Key: {key_response.key}")
    print(f"User ID: {key_response.user_id}")
```

## Tool Calling - Function Calling

Use function calling to enable models to invoke external tools. Define tool schemas and handle tool calls in your application.

```python
from openrouter import OpenRouter
import os
import json

def get_weather(location: str, unit: str = "celsius") -> str:
    # Mock weather data
    return json.dumps({"location": location, "temperature": 22, "unit": unit, "condition": "sunny"})

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City and country, e.g., 'London, UK'"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["location"]
                }
            }
        }
    ]

    messages = [{"role": "user", "content": "What's the weather like in Paris?"}]

    response = client.chat.send(
        model="openai/gpt-4",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    # Handle tool calls
    if response.choices[0].message.tool_calls:
        for tool_call in response.choices[0].message.tool_calls:
            if tool_call.function.name == "get_weather":
                args = json.loads(tool_call.function.arguments)
                result = get_weather(**args)

                # Send tool result back
                messages.append(response.choices[0].message)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

                final_response = client.chat.send(
                    model="openai/gpt-4",
                    messages=messages,
                    tools=tools
                )
                print(final_response.choices[0].message.content)
```

## Error Handling

Handle various error types returned by the API including authentication errors, rate limits, and provider-specific issues.

```python
from openrouter import OpenRouter
from openrouter.errors import (
    UnauthorizedResponseError,
    TooManyRequestsResponseError,
    PaymentRequiredResponseError,
    BadRequestResponseError,
    InternalServerResponseError,
    ProviderOverloadedResponseError,
    ChatError
)
import os

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as client:
    try:
        response = client.chat.send(
            model="openai/gpt-4",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.choices[0].message.content)

    except UnauthorizedResponseError as e:
        print(f"Authentication failed: {e.data.message}")

    except PaymentRequiredResponseError as e:
        print(f"Insufficient credits: {e.data.message}")

    except TooManyRequestsResponseError as e:
        print(f"Rate limited: {e.data.message}")

    except BadRequestResponseError as e:
        print(f"Invalid request: {e.data.message}")

    except ProviderOverloadedResponseError as e:
        print(f"Provider overloaded, try again: {e.data.message}")

    except InternalServerResponseError as e:
        print(f"Server error: {e.data.message}")

    except ChatError as e:
        print(f"Chat error: {e.error.message}")
```

## Debugging

Enable debug logging to troubleshoot SDK requests and responses. Configure custom loggers or use environment variables for debugging.

```python
from openrouter import OpenRouter
import logging
import os

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("openrouter")

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
    debug_logger=logger
) as client:
    response = client.chat.send(
        model="openai/gpt-4",
        messages=[{"role": "user", "content": "Hello!"}]
    )

# Alternative: Set OPENROUTER_DEBUG=true environment variable
```

## Summary

The OpenRouter Python SDK provides a comprehensive interface for accessing 300+ AI models through a unified API. Primary use cases include building chatbots and conversational AI applications, implementing AI-powered features in web and mobile applications, batch processing of text generation tasks, semantic search using embeddings, and multi-model comparison and routing. The SDK is particularly valuable for applications requiring model diversity, cost optimization through provider routing, or enterprise features like guardrails and usage analytics.

Integration follows standard Python patterns with context managers for resource management, Pydantic models for type safety, and both sync and async interfaces for different application architectures. For production deployments, combine API key management with guardrails to enforce usage policies, use the analytics endpoints for cost monitoring, and leverage provider preferences for optimizing latency or cost. The SDK's automatic retries and comprehensive error handling make it suitable for building resilient AI applications at scale.
