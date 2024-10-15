import { FormEvent, useState } from 'react'
import './App.css'

type AuthStatus = "AUTHENTICATED" | "UNAUTHENTICATED" | "ERROR" | "LOADING" | "FINISHED"

function App() {
  const [status, setStaus] = useState<AuthStatus>("UNAUTHENTICATED")
  const [error, setError] = useState(null)

  const login = async (data: { email: string, password: string }) => {
    try {
      setError(null)
      setStaus("LOADING")
      const r = await fetch(`${import.meta.env['VITE_API_URL']}/login/`, {
        method: "POST",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })

      if (!r.ok) {
        setError(await r.json())
        throw new Error(JSON.stringify(await r.json()))
      }
      console.log(await r.json())
      setStaus("AUTHENTICATED")
    } catch (e) {
      setStaus("UNAUTHENTICATED")
      console.log(e)
    }
  }

  return (
    <div className='flex w-full flex-col mx-auto white p-8 justify-center h-screen'>
      <div className='absolute top-0 left-0 right-0 bottom-0 -z-10 bg-[radial-gradient(#e66465, #9198e5)]'></div>
      {
        status === "AUTHENTICATED" &&
        <>
          <h1 className='text-2xl text-black mb-4'>Authenticated</h1>
          <button className='bg-emerald-500 p-4 text-white font-bold' onClick={() => {
            setStaus('UNAUTHENTICATED')
          }}>LOGOUT</button>
        </>
      }
      {
        status === "UNAUTHENTICATED" &&
        <form className='flex flex-col md:w-1/3 w-full gap-4 self-center bg-white p-8 rounded-lg shadow-lg shadow-purple-200' onSubmit={(e: FormEvent<HTMLFormElement>) => {
          e.preventDefault()
          const form = e.currentTarget;
          const formData = new FormData(form);

          // Convert FormData to a plain object
          const formValues = Object.fromEntries(formData.entries());

          console.log('Form data:', formValues['email']);
          login({ email: formValues['email'].toString(), password: formValues['password'].toString() })
        }}>
          <p className='text-red-500 font-bold'>{error ? error['message'] : null}</p>
          <h1 className='text-2xl font-bold text-center'>Enter your credentials</h1>
          <input required autoFocus className='border-[1px] border-gray-300 px-4 py-2 rounded-md' type='email' placeholder='admin@test.com' name='email' />
          <input required className='border-[1px] border-gray-300 px-4 py-2 rounded-md' type='password' placeholder='password' name='password' />
          <button className='self-start bg-purple-600 px-6 py-2 rounded-md text-white font-medium'>Continue</button>
        </form>
      }
    </div>
  )
}

export default App
