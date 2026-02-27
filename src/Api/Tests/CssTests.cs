using Xunit;
using AngleSharp;
using AngleSharp.Dom;
using System.Threading.Tasks;

namespace Api.Tests
{
    public class CssTests
    {
        [Fact]
        public async Task MainContent_ShouldHaveCorrectStyles()
        {
            var config = Configuration.Default.WithDefaultLoader();
            var context = BrowsingContext.New(config);
            var document = await context.OpenAsync("http://localhost:5000");

            var main = document.QuerySelector("main");
            Assert.NotNull(main);
            Assert.Equal("20px", main.GetStyle().Padding);
            Assert.Equal("800px", main.GetStyle().MaxWidth);
            Assert.Equal("0 auto", main.GetStyle().Margin);
        }

        [Fact]
        public async Task Header_ShouldBeResponsive()
        {
            var config = Configuration.Default.WithDefaultLoader();
            var context = BrowsingContext.New(config);
            var document = await context.OpenAsync("http://localhost:5000");

            var header = document.QuerySelector("header h1");
            Assert.NotNull(header);
            Assert.Equal("24px", header.GetStyle().FontSize);

            // Simulate a smaller screen
            document.DefaultView.ResizeTo(500, 800);
            Assert.Equal("20px", header.GetStyle().FontSize);
        }
    }
}