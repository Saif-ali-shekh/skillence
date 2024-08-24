from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from App_Models.models import Question, Option


class DashboardViews(View):
    template_name = 'base/base.html'
    
    def get(self, request):
        return render(request, self.template_name)
        
class AdminAddQuestionView(View):
    template_name='quiz/admin_add_question.html'
    def get(self, request):
        return render(request, self.template_name)  

    def post(self, request):
        question_text = request.POST.get('question')
        options = [request.POST.get(f'option{i}') for i in range(1, 5)]
        print(options)
        correct_option = int(request.POST.get('correct_option'))

        if not question_text or not all(options) or correct_option not in range(1, 5):
            messages.error(request, "All fields are required.")
            return redirect('admin_add_question')

        question = Question.objects.create(text=question_text)
        for i, option_text in enumerate(options):
            Option.objects.create(
                question=question,
                text=option_text,
                is_correct=(i + 1 == correct_option)
            )
        messages.success(request, "Question added successfully.")
        return redirect('admin_add_question')

# class UserQuizView(View):
#     def get(self, request):
#         questions = Question.objects.all()
#         paginator = Paginator(questions, 10)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(request, 'quiz/quiz.html', {'page_obj': page_obj})

#     def post(self, request):
#         # Handle option selection and navigation
#         pass

# class SubmitQuizView(View):
#     def post(self, request):
#         # Calculate and show score
#         pass

from django.shortcuts import render, redirect, get_object_or_404
import random

# class UserQuizView(View):
#     def get(self, request):
#         question_ids = list(Question.objects.values_list('id', flat=True))
#         random.shuffle(question_ids)
#         questions = Question.objects.filter(id__in=question_ids)
#         paginator = Paginator(questions, 2)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(request, 'quiz/quiz.html', {'page_obj': page_obj})

#     def post(self, request):
#         selected_answers = request.session.get('selected_answers', {})
#         new_answers = {int(key.split('_')[1]): int(value) for key, value in request.POST.items() if key.startswith('question_')}
#         selected_answers.update(new_answers)
#         request.session['selected_answers'] = selected_answers
#         return redirect('submit_quiz')
# class SubmitQuizView(View):
#     def get(self, request):
#         selected_answers = request.session.get('selected_answers', {})
#         total_questions = len(selected_answers)
#         correct_count = 0

#         for question_id, selected_option_id in selected_answers.items():
#             option = get_object_or_404(Option, id=selected_option_id)
#             if option.is_correct:
#                 correct_count += 1

#         wrong_count = total_questions - correct_count
#         score_percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0

#         context = {
#             'total_questions': total_questions,
#             'correct_count': correct_count,
#             'wrong_count': wrong_count,
#             'score_percentage': score_percentage,
#         }
#         return render(request, 'quiz/result.html', context)

from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.urls import reverse
import random

from django.db.models import Count

class UserQuizView(View):
    def get(self, request):
        # Fetch 15 unique random questions if not already in session
        if not request.session.get('question_ids'):
            question_ids = list(Question.objects.values_list('id', flat=True))
            if len(question_ids) > 15:
                question_ids = random.sample(question_ids, 15)
            else:
                random.shuffle(question_ids)
            request.session['question_ids'] = question_ids
        else:
            question_ids = request.session['question_ids']
        
        # Pagination setup
        paginator = Paginator(question_ids,15)  # Adjust the number of questions per page as needed
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # Fetch questions for the current page
        questions = Question.objects.filter(id__in=page_obj.object_list)

        # Retrieve selected answers from session
        selected_answers = request.session.get('selected_answers', {})

        context = {
            'questions': questions,
            'page_obj': page_obj,
            'selected_answers': selected_answers,
        }
        return render(request, 'quiz/quiz.html', context)

    def post(self, request):
        selected_answers = request.session.get('selected_answers', {})
        
        # Extract answers from POST data
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                selected_answers[question_id] = int(value)
        
        request.session['selected_answers'] = selected_answers

        action = request.POST.get('action')
        current_page = int(request.POST.get('current_page', 1))
        paginator = Paginator(request.session['question_ids'], 2)

        if action == 'next':
            next_page = current_page + 1
            if next_page <= paginator.num_pages:
                return redirect(f"{reverse('quiz')}?page={next_page}")
        elif action == 'previous':
            prev_page = current_page - 1
            if prev_page >= 1:
                return redirect(f"{reverse('quiz')}?page={prev_page}")
        elif action == 'submit':
            return redirect('submit_quiz')

        return redirect('quiz')

class SubmitQuizView(View):
    def get(self, request):
        selected_answers = request.session.get('selected_answers', {})
        total_questions = 15  # Set to 15 as we only select 15 questions
        correct_answers = 0
        results = []

        for question_id, selected_option_id in selected_answers.items():
            question = Question.objects.get(id=question_id)
            selected_option = Option.objects.get(id=selected_option_id)
            correct_option = Option.objects.filter(question=question, is_correct=True).first()
            is_correct = selected_option.is_correct

            if is_correct:
                correct_answers += 1

            results.append({
                'question': question,
                'selected_option': selected_option,
                'correct_option': correct_option,
                'is_correct': is_correct,
            })

        score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

        context = {
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'score_percentage': round(score_percentage, 2),
            'results': results,
        }

        # Clear session data
        request.session.pop('selected_answers', None)
        request.session.pop('question_ids', None)

        return render(request, 'quiz/result.html', context)