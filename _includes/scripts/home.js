const searchParams = new URLSearchParams(window.location.search);
if (searchParams.has('lptag')) {
    const newUrl = "https://link.coupang.com/re/AFFSDP?" + searchParams.toString();
    window.location.href = newUrl;
}