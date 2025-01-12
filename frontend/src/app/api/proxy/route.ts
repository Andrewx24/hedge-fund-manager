import { auth } from '@clerk/nextjs/server'

export async function GET(request: Request) {
  const { userId } = auth();
  
  if (!userId) {
    return new Response('Unauthorized', { status: 401 });
  }

  // Forward request to Python backend
  const response = await fetch('http://localhost:8000/portfolio', {
    headers: {
      'Authorization': `Bearer ${userId}`,
    },
  });

  return response;
}