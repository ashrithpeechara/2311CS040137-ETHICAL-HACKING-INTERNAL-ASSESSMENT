// ==============================================================================
// Dashboard Interactive JavaScript Controller
// ==============================================================================

async function executeSqliTest(type) {
    const outputEl = document.getElementById("sqliOutput");
    const endpointType = document.querySelector('input[name="targetEngine"]:checked').value; // "vulnerable" or "secure"
    let payload = "";
    let url = "";

    if (type === "auth") {
        payload = document.getElementById("authPayload").value;
        url = `/api/${endpointType}/login`;
        outputEl.innerHTML = `<span style="color: var(--cyber-cyan);">[*] Sending POST request to ${url}...</span>\nPayload: ${payload}`;

        try {
            const resp = await fetch(url, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: payload, password: "dummy_password" })
            });
            const data = await resp.json();
            formatResult(outputEl, data, resp.status);
        } catch (err) {
            outputEl.innerHTML = `<span style="color: var(--cyber-red);">[-] Error: ${err.message}</span>`;
        }
    } else if (type === "search") {
        payload = document.getElementById("searchPayload").value;
        url = `/api/${endpointType}/search?q=${encodeURIComponent(payload)}`;
        outputEl.innerHTML = `<span style="color: var(--cyber-cyan);">[*] Sending GET request to ${url}...</span>`;

        try {
            const resp = await fetch(url);
            const data = await resp.json();
            formatResult(outputEl, data, resp.status);
        } catch (err) {
            outputEl.innerHTML = `<span style="color: var(--cyber-red);">[-] Error: ${err.message}</span>`;
        }
    } else if (type === "user") {
        payload = document.getElementById("userPayload").value;
        url = `/api/${endpointType}/user/${encodeURIComponent(payload)}`;
        outputEl.innerHTML = `<span style="color: var(--cyber-cyan);">[*] Sending GET request to ${url}...</span>`;

        try {
            const resp = await fetch(url);
            const data = await resp.json();
            formatResult(outputEl, data, resp.status);
        } catch (err) {
            outputEl.innerHTML = `<span style="color: var(--cyber-red);">[-] Error: ${err.message}</span>`;
        }
    }
}

function formatResult(el, data, status) {
    let statusClass = status === 200 ? "color: var(--cyber-green);" : "color: var(--cyber-amber);";
    let formatted = `\n<span style="${statusClass}">HTTP Status: ${status}</span>\n\n`;
    formatted += JSON.stringify(data, null, 2);
    el.innerHTML = formatted;
}

async function triggerLiveRetest() {
    const btn = document.getElementById("retestBtn");
    const statusBox = document.getElementById("retestStatusBox");
    if (btn) btn.innerText = "Running Retest Engine...";

    try {
        const resp = await fetch("/api/run-retests", { method: "POST" });
        const data = await resp.json();
        if (statusBox) {
            statusBox.innerHTML = `<span style="color: var(--cyber-green);">[+] Retest Completed: ${data.total_passed}/${data.total_retested} Vectors Remediated</span>`;
        }
        setTimeout(() => location.reload(), 1500);
    } catch (err) {
        if (statusBox) statusBox.innerHTML = `<span style="color: var(--cyber-red);">[-] Retest Failed: ${err.message}</span>`;
    } finally {
        if (btn) btn.innerText = "Re-Run Automated Verification";
    }
}
