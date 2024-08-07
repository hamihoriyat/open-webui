<script>
    export let pricingOptions = [
        {
            title: 'نقره‌ای',
            description: 'امکان استفاده از مدل های حرفه ای GPT-4o-mini و Claude-3-Haiku و Llama70b و Mistral',
            price: '۹۹,۰۰۰ تومان/ ماهیانه',
            features: [
                'دسترسی به مدل‌هایGPT-4o-mini و Llama و Claude-3-Haiku و Mistral و ...',
                'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
                'محدودیت پرامپت ورودی ۵۰۰۰۰ کاراکتر',
                'بدون محدودیت آپلود فایل',
                'بدون محدودیت تعداد پرامپت'
            ],
            popular: false,
        },
        {
            title: 'طلایی',
            description: 'امکان استفاده از مدل های حرفه ای GPT 4O و Claude Sonnet 3.5 و Llama405B و Mistral large',
            price: '۴۹۹,۰۰۰ تومان/ ماهیانه',
            features: [
                'دسترسی به تمام مدل‌های Claude و GPT و Gemini و Llama و Mistral و ...',
                'دسترسی به مدل‌ پردازش تصویر  Diffusion',
                'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
                'محدودیت پرامپت ورودی ۱۰۰۰۰۰ کاراکتر',
                'بدون محدودیت آپلود فایل',
                'بدون محدودیت تعداد پرامپت'
            ],
            popular: false,
        },
        {
            title: 'سازمانی',
            description: 'کامل ترین دسترسی به تمامی امکانات بدون هیچگونه محدودیتی به همراه API',
            price: '۲,۹۹۹,۰۰۰ تومان/ ماهیانه',
            features: [
                'دسترسی به تمام مدل‌های Claude و GPT و Gemini',
                'دسترسی به مدل‌های Llama3، Codegemma و ...',
				'دسترسی به مدل‌ پردازش تصویر  Diffusion',
                'استفاده از سرویس مکالمه صوتی با دستیار هوشمند',
                'سرویس API دسترسی به تمامی مدل‌ها',
                'امکان تعریف مدل‌های مخصوص ',
                'بدون محدودیت تعداد کاربر',
                'بدون محدودیت آپلود فایل',
                'بدون محدودیت پرامپت ورودی'
            ],
            popular: false,
        },
    ];

    // Function to split price string into parts for formatting
    function formatPrice(price) {
        const parts = price.split('ماهیانه');
        return {
            main: parts[0],
            monthly: parts.length > 1 ? 'ماهیانه' : ''
        };
    }
</script>

<div class="bg-gray-900 py-10 flex flex-col min-h-screen overflow-y-scroll justify-center" dir="rtl">
    <div class="max-w-7xl mx-auto px-4 text-white max-h-screen overflow-y-scroll no-scrollbar">
        <h2 class="text-3xl font-bold text-center mb-2">عضویت ویژه</h2>
        <p class="text-center mb-8">بدون محدودیت از بهترین مدل‌های هوش مصنوعی بهره‌مند شوید</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            {#each pricingOptions as option}
            <div class={`bg-gray-800 rounded-lg shadow-lg p-6 flex flex-col justify-between h-full ${option.popular ? 'border-4 border-orange-500' : ''}`}>
                <div>
                    <h3 class="text-xl font-semibold mb-2 font-mona center">{option.title} {option.popular ? '<span class="text-orange-500">(Most popular)</span>' : ''}</h3>
                    <p class="text-gray-400 mb-4">{option.description}</p>
                    <p class="text-2xl font-bold mb-4">
                        {#if formatPrice(option.price).main}
                            {formatPrice(option.price).main.split('تومان/')[0]}
                            <span class="text-sm smaller-text">تومان/</span>
                        {/if}
                        {#if formatPrice(option.price).monthly}
                            <span class="text-sm smaller-text">{formatPrice(option.price).monthly}</span>
                        {/if}
                    </p>
                    <ul class="mb-6">
                        {#each option.features as feature}
                        <li class={`text-gray-300 mb-2 flex items-center ${feature.includes('بدون محدودیت') ? 'highlight' : ''}`}>
                            <svg class={`w-5 h-5 mr-2 ${feature.includes('بدون محدودیت') ? 'highlight-box' : 'text-orange-500'}`} fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M10 15.293l-3.293-3.293a1 1 0 011.414-1.414L10 12.586l2.879-2.879a1 1 0 011.414 1.414L10 15.293z" clip-rule="evenodd"/>
                                <path fill-rule="evenodd" d="M10 4.293l-3.293 3.293a1 1 0 001.414 1.414L10 6.414l2.879 2.879a1 1 0 001.414-1.414L10 4.293z" clip-rule="evenodd"/>
                            </svg>
                            {feature}
                        </li>
                        {/each}
                    </ul>
                </div>
                <button class="bg-orange-400 text-white py-2 px-4 rounded-lg mt-auto hover:bg-red-500">خرید اشتراک</button>
            </div>
            {/each}
        </div>
        <!-- Support Explanation Lines -->
         <div class="container">
     
        <div class="column text-center">
            <a referrerpolicy='origin' target='_blank' href='https://trustseal.enamad.ir/?id=515612&Code=AKDQYXMezOsa9acJtXZe0XoOOOXrWkrZ'><img referrerpolicy='origin' src='https://trustseal.enamad.ir/logo.aspx?id=515612&Code=AKDQYXMezOsa9acJtXZe0XoOOOXrWkrZ' alt='' style='cursor:pointer' code='AKDQYXMezOsa9acJtXZe0XoOOOXrWkrZ'></a>
        </div>
        <div class="text-center text-gray-400 column large">
            <p>در صورت نیاز به راهنمایی وارد این <a href="https://blog.azadai.ir" class="text-white">لینک</a> شوید</p>
            <p>ایمیل پشتیبانی: support@azadai.ir</p>
            <br/>
			<p>برای امکان دسترسی به سرویس API برای افراد حقیقی به پشتیبانی ایمیل ارسال کنید.</p>
        </div>
        <div class="column">
            <span></span>
        </div>
    </div>
    </div>
</div>

<style>
    .font-mona {
        font-family: 'Vazir-Medium', -apple-system, 'Vazir-Medium', 'Inter', ui-sans-serif, system-ui,
            'Segoe UI', Roboto, Ubuntu, Cantarell, 'Noto Sans', sans-serif, 'Helvetica Neue', Arial,
            'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
    }
    h2 {
        font-family: 'Vazir-Medium'
    }
    /* Styles for highlighted features */
    .highlight {
        font-weight: bold;
        color: #22C55E;
    }
    .highlight-box {
        fill: #F97316;
    }

    /* Smaller text for ۰ */
    .smaller-text {
        font-size: 0.85rem; /* Adjust the value as needed */
    }

    .container {
        display: flex;
        justify-content: space-around; /* Distribute space evenly */
        align-items: flex-start; /* Align items at the start of the flex container's cross axis */
        margin-top: 2rem; /* Adds some space from the top */
        color: gray; /* Text color */
    }
    .column {
        flex: 1; /* Each column takes equal space */
        padding: 1rem; /* Adds some padding inside the columns */
        text-align: center; /* Centers the text inside each column */
    }
    .column.large {
        flex: 2; /* Makes this column larger */
    }
</style>