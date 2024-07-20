<script>
  export let pricingOptions = [
    {
      title: 'نقره ای',
      description: 'با ثبت نام اولیه در AzadAI می توانید از این طرح استفاده نمایید',
      price: 'رایگان',
      features: [
        'دسترسی رایگان به مدل هایGPT-4o-miniوGPT-3.5-Turbo',
        'دسترسی رایگان به مدل های Llama3، Codegemma، phi3 و ...',
        'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
        ' بدون محدودیت آپلود فایل',
        'بدون محدودیت تعداد پرامپت',
        'محدودیت پرامپت ورودی ۲۰۰۰ کاراکتر'
    
      ],
      button_name:'خرید اشتراک لازم نیست',
      popular: false,
    },
    {
      title: 'طلایی',
      description: 'امکان استفاده از مدل های حرفه ای GPT 4O و Claude Sonnet 3.5 و ...',
      price: '۳۹۹ هزار تومان/ماهیانه',
      features: [
        'دسترسی به تمام مدل های Claude و GPT و Gemini',
        'دسترسی رایگان به مدل های Llama3، Codegemma، phi3 و ...',
        'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
        ' بدون محدودیت آپلود فایل',
        'بدون محدودیت تعداد پرامپت',
        'محدودیت پرامپت ورودی ۴۰۰۰ کاراکتر'
      ],
      button_name:'خرید اشتراک',
      popular: false,
    },
    {
      title: 'سازمانی',
      description: 'کامل ترین دسترسی به تمامی امکانات بدون هیچگونه محدودیتی به همراه API',
      price: '۲۹۹۹ هزار تومان/ماهیانه',
      features: [
        'دسترسی به تمام مدل های Claude و GPT و Gemini',
        'دسترسی رایگان به مدل های Llama3، Codegemma، phi3 و ...',
        'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
        'آپلود بدون محدودیت فایل',
        'سرویس API دسترسی به تمامی مدل ها',
        'امکان تعریف مدل های مخصوص  یا محدود سازی مدل های کاربران ',
        'بدون محدودیت پرامپت ورودی',
        'بدون محدودیت تعداد کاربر'
      ],
      button_name:'خرید اشتراک',
      popular: false,
    },
  ];
  function goToHome(){
    window.location.href="/";
  }
</script>

<div class="bg-gray-900 py-10 flex flex-col min-h-screen justify-center" dir="rtl">
  <div class="max-w-7xl mx-auto px-4 text-white">
    <h2 class="text-2xl font-bold text-center mb-5">ممنون که برای حمایت از ما به این صفحه اومدی.ولی هنوز امکان پرداخت فراهم نشده،پس به استفاده رایگان ادامه بده!</h2>
    <div class="text-center mb-4">
    <button on:click={()=>{goToHome()}} class="bg-orange-400 text-white py-2 px-4 rounded-lg mt-auto">بازگشت</button>
  </div>
    <h2 class="text-3xl font-bold text-center mb-2">عضویت ویژه</h2>
    <p class="text-center mb-8">با خرید هریک از پلن های اشتراک ویژه،از دنیای بدون تحریم مدل های زبانی بهره مند شوید</p>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      {#each pricingOptions as option}
        <div class={`bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col justify-between h-full ${option.popular ? 'border-4 border-blue-500' : ''}`}>
          <div>
            <h3 class="text-xl font-semibold mb-2">{option.title} {option.popular ? '<span class="text-blue-500">(Most popular)</span>' : ''}</h3>
            <p class="text-gray-400 mb-4">{option.description}</p>
            <p class="text-2xl font-bold mb-4">{option.price}</p>
            <ul class="mb-6">
              {#each option.features as feature}
                <li class="text-gray-300 mb-2 flex items-center">
                  <svg class="w-5 h-5 text-orange-500 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M10 15.293l-3.293-3.293a1 1 0 011.414-1.414L10 12.586l2.879-2.879a1 1 0 011.414 1.414L10 15.293z" clip-rule="evenodd"/>
                    <path fill-rule="evenodd" d="M10 4.293l-3.293 3.293a1 1 0 001.414 1.414L10 6.414l2.879 2.879a1 1 0 001.414-1.414L10 4.293z" clip-rule="evenodd"/>
                  </svg>
                  {feature}
                </li>
              {/each}
            </ul>
          </div>
          <button class="bg-orange-400 text-white py-2 px-4 rounded-lg mt-auto">{option.button_name}</button>
        </div>
      {/each}
    </div>
    
  </div>
</div>

<style>
	.font-mona {
		font-family: 'Vazir-Medium', -apple-system, 'Vazir-Medium', 'Inter', ui-sans-serif, system-ui,
			'Segoe UI', Roboto, Ubuntu, Cantarell, 'Noto Sans', sans-serif, 'Helvetica Neue', Arial,
			'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
	}
</style>